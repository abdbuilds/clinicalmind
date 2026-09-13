"""
load_patients_to_mongo.py — flatten Synthea FHIR bundles into patient documents
and bulk-load them into MongoDB (ClinicalMind, Day 6).

Reads:  synthea/output/fhir/*.json   (one FHIR Bundle per patient)
Writes: MongoDB clinicalmind.patients (one denormalized doc per patient)

Run:
    source .venv/bin/activate
    python3 scripts/load_patients_to_mongo.py
"""

import glob
import json
import os
import sys
from datetime import datetime, timezone

from pymongo import ReplaceOne

# make `db` package importable when run as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import get_collection  # noqa: E402

FHIR_DIR = os.environ.get("FHIR_DIR", "synthea/output/fhir")
BATCH = 500

# LOINC codes for the vitals we keep (latest value each)
VITALS = {
    "8480-6": "bp_systolic",
    "8462-4": "bp_diastolic",
    "8867-4": "heart_rate",
    "2339-0": "glucose",
    "2345-7": "glucose",
}


def _age(birth_date: str | None) -> int | None:
    if not birth_date:
        return None
    try:
        b = datetime.strptime(birth_date[:10], "%Y-%m-%d")
        today = datetime.now(timezone.utc)
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))
    except ValueError:
        return None


def _display(codeable: dict) -> str | None:
    if not codeable:
        return None
    if codeable.get("text"):
        return codeable["text"]
    coding = codeable.get("coding") or []
    return coding[0].get("display") if coding else None


def flatten_bundle(bundle: dict) -> dict | None:
    """Turn one Synthea FHIR bundle into a single patient document."""
    resources = [e.get("resource", {}) for e in bundle.get("entry", [])]
    patient = next((r for r in resources if r.get("resourceType") == "Patient"), None)
    if not patient:
        return None

    name = (patient.get("name") or [{}])[0]
    given = " ".join(name.get("given", []))
    family = name.get("family", "")
    addr = (patient.get("address") or [{}])[0]

    doc = {
        "_id": patient.get("id"),
        "name": {"given": given, "family": family, "full": f"{given} {family}".strip()},
        "gender": patient.get("gender"),
        "birthDate": patient.get("birthDate"),
        "age": _age(patient.get("birthDate")),
        "address": {
            "city": addr.get("city"),
            "state": addr.get("state"),
            "postalCode": addr.get("postalCode"),
        },
        "conditions": [],
        "medications": [],
        "vitals": {},
        "last_encounter_date": None,
        "source": "synthea",
        "ingested_at": datetime.now(timezone.utc),
    }

    seen_cond, seen_med = set(), set()
    latest_vital_date: dict[str, str] = {}
    latest_encounter = None

    for r in resources:
        rt = r.get("resourceType")

        if rt == "Condition":
            disp = _display(r.get("code"))
            if disp and disp not in seen_cond:
                seen_cond.add(disp)
                doc["conditions"].append({
                    "display": disp,
                    "clinicalStatus": _display(r.get("clinicalStatus")) or (
                        (r.get("clinicalStatus", {}).get("coding") or [{}])[0].get("code")),
                    "onsetDate": r.get("onsetDateTime"),
                })

        elif rt == "MedicationRequest":
            disp = _display(r.get("medicationCodeableConcept"))
            if disp and disp not in seen_med:
                seen_med.add(disp)
                doc["medications"].append({
                    "display": disp,
                    "status": r.get("status"),
                    "authoredOn": r.get("authoredOn"),
                })

        elif rt == "Observation":
            eff = r.get("effectiveDateTime") or ""
            # standalone vital
            code = ((r.get("code", {}).get("coding") or [{}])[0]).get("code")
            if code in VITALS and "valueQuantity" in r:
                key = VITALS[code]
                if eff >= latest_vital_date.get(key, ""):
                    latest_vital_date[key] = eff
                    doc["vitals"][key] = r["valueQuantity"].get("value")
            # BP panel with components
            for comp in r.get("component", []):
                ccode = ((comp.get("code", {}).get("coding") or [{}])[0]).get("code")
                if ccode in VITALS and "valueQuantity" in comp:
                    key = VITALS[ccode]
                    if eff >= latest_vital_date.get(key, ""):
                        latest_vital_date[key] = eff
                        doc["vitals"][key] = comp["valueQuantity"].get("value")

        elif rt == "Encounter":
            start = (r.get("period") or {}).get("start")
            if start and (latest_encounter is None or start > latest_encounter):
                latest_encounter = start

    doc["last_encounter_date"] = latest_encounter
    return doc


def main() -> None:
    files = [
        f for f in glob.glob(os.path.join(FHIR_DIR, "*.json"))
        if not os.path.basename(f).startswith(("hospitalInformation", "practitionerInformation"))
    ]
    if not files:
        print(f"No FHIR bundles found in {FHIR_DIR}. Has Synthea finished generating?")
        sys.exit(1)

    print(f"Found {len(files)} patient bundles. Loading into MongoDB...")
    col = get_collection("patients")

    ops, loaded, skipped = [], 0, 0
    for i, path in enumerate(files, 1):
        try:
            with open(path) as fh:
                bundle = json.load(fh)
            doc = flatten_bundle(bundle)
            if not doc or not doc.get("_id"):
                skipped += 1
                continue
            ops.append(ReplaceOne({"_id": doc["_id"]}, doc, upsert=True))
        except (json.JSONDecodeError, KeyError) as e:
            skipped += 1
            continue

        if len(ops) >= BATCH:
            col.bulk_write(ops, ordered=False)
            loaded += len(ops)
            ops = []
            print(f"  ...{loaded} loaded")

    if ops:
        col.bulk_write(ops, ordered=False)
        loaded += len(ops)

    # helpful indexes for the query patterns we'll use later
    col.create_index("name.family")
    col.create_index("gender")
    col.create_index("conditions.display")
    col.create_index("birthDate")

    print(f"\n✅ Done. Upserted {loaded} patients (skipped {skipped}).")
    print(f"   Total docs in clinicalmind.patients: {col.count_documents({})}")


if __name__ == "__main__":
    main()
