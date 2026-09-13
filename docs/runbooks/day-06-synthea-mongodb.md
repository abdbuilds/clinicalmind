# Day 06 — Generate patients with Synthea → MongoDB

**Course position:** Month 1 · Week 1 · Day 6
**GitHub issue:** #6
**Goal (plain):** Generate bulk synthetic FHIR patients with Synthea and bulk-load them into MongoDB.
**Definition of done:** `clinicalmind.patients` in MongoDB holds the patients; you can browse them in Compass and identify Patient/Condition/Medication fields.

> **Deviation from the course:** the course stores 100 FHIR files in `data/sample/`.
> Per the developer's choice, we scale up and load into **MongoDB** instead (with
> 3 sample bundles still committed to `data/sample/` for reference). S3 (Day 7)
> and the Knowledge Base still use files.

---

## Concepts (simple + examples)

- **Synthea** = MITRE's synthetic patient generator. Each patient = one FHIR **Bundle**.
  All data is generated, not real → **zero HIPAA risk**.
- **Denormalized document** = one MongoDB doc per patient with everything inline
  (conditions, meds, vitals). MongoDB likes this; it matches "get one patient".
- **Bulk write** = insert many docs in batches (`ReplaceOne` upserts) instead of
  one-at-a-time — fast and idempotent (safe to re-run).

---

## Steps

1. Ensure Java 17, a running MongoDB (`mongodb://localhost:27017`), and `pip install -r requirements.txt` (adds `pymongo`).
2. One command:
   ```bash
   ./data/generate/generate.sh 1000
   ```
   (downloads Synthea once → generates → flattens → bulk-loads MongoDB)
3. Browse `clinicalmind.patients` in **MongoDB Compass**.

Manual equivalent:
```bash
cd synthea && java -jar synthea.jar -p 1000 --exporter.baseDirectory=./output --exporter.fhir.export=true
python3 scripts/load_patients_to_mongo.py
```

---

## Verify it worked

- [ ] `clinicalmind.patients` count ≈ number generated
- [ ] A document has `name`, `gender`, `age`, `conditions[]`, `medications[]`, `vitals`
- [ ] Visible in Compass

---

## Files

- `db/connection.py` — secure MongoDB client (env-based URI, retry/backoff)
- `db/SCHEMA.md` — the patient document schema
- `scripts/load_patients_to_mongo.py` — FHIR bundle → patient doc bulk loader
- `data/generate/generate.sh` — one-command reproducer

---

## ⚠️ Gotchas & Deviations

- **Synthea arg syntax:** use `--exporter.baseDirectory=./output` (with `=`), and
  do **not** pass `-c <file>` unless the properties file exists — a bad arg makes
  Synthea print its usage/help and exit without generating. First run failed this
  way; fixed by using the `=` form and dropping the bogus `-c`.
- **Compass ≠ server:** Compass is only the GUI; a `mongod` server must be running
  (it already was, on `localhost:27017`).
- **Data location:** raw FHIR (`synthea/output/`) and the jar are git-ignored (bulk);
  the source of truth is MongoDB + 3 committed samples in `data/sample/`.
