# Synthetic patient data (Synthea → MongoDB)

We generate **synthetic** FHIR R4 patients with [Synthea](https://github.com/synthetichealth/synthea)
(by MITRE) and load them into **MongoDB**. All data is mathematically generated —
**not** derived from real people, so there is **zero HIPAA risk**.

## What is Synthea?
A synthetic patient generator. Each patient is a **FHIR Bundle** (a container
holding all their resources): `Patient`, `Condition`, `MedicationRequest`,
`Observation` (labs/vitals), `Encounter` (visits), etc.

## One command
```bash
./data/generate/generate.sh 1000      # generate 1000 patients + load into MongoDB
```
This: downloads Synthea (once) → generates FHIR bundles into `synthea/output/fhir/`
→ flattens each into a patient document → bulk-loads `clinicalmind.patients`.

Prerequisites: Java 17, a running MongoDB (`mongodb://localhost:27017`), and the
project `.venv` with `pymongo` (`pip install -r requirements.txt`).

## Where the data lives
- **Raw FHIR bundles:** `synthea/output/fhir/*.json` (git-ignored — large/bulk)
- **Loaded documents:** MongoDB `clinicalmind.patients` (browse in Compass)
- **Committed samples:** 3 example bundles in `data/sample/` (for reference)

## Document schema
See [`db/SCHEMA.md`](../../db/SCHEMA.md).
