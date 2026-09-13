# MongoDB schema — `clinicalmind` database

MongoDB is document-oriented, so we **denormalize** each FHIR patient bundle into
one self-contained document. Bounded (active conditions/meds + latest vitals only)
so documents stay well under Mongo's 16 MB limit and match what the
`get_patient_summary` agent tool will need.

## Collection: `patients`

```jsonc
{
  "_id": "72ea0782-...",              // FHIR Patient.id — stable, dedup-safe
  "name": {
    "given":  "Kacy732 Rosamaria757",
    "family": "Robel940",
    "full":   "Kacy732 Rosamaria757 Robel940"
  },
  "gender": "female",
  "birthDate": "2019-09-13",
  "age": 7,                            // computed at load time
  "address": { "city": "Salem", "state": "MA", "postalCode": "01907" },

  "conditions": [                      // deduped by display
    { "display": "Hypertension", "clinicalStatus": "active", "onsetDate": "2018-..." }
  ],
  "medications": [
    { "display": "lisinopril 10 MG", "status": "active", "authoredOn": "2019-..." }
  ],
  "vitals": {                          // latest value each (from Observations)
    "bp_systolic": 128, "bp_diastolic": 82, "heart_rate": 72, "glucose": 95
  },
  "last_encounter_date": "2024-11-...",

  "source": "synthea",
  "ingested_at": "2026-...Z"
}
```

## FHIR → document mapping

| Document field | FHIR source |
|---|---|
| `_id`, `name`, `gender`, `birthDate`, `address` | `Patient` |
| `conditions[]` | `Condition` (code, clinicalStatus, onsetDateTime) |
| `medications[]` | `MedicationRequest` (medicationCodeableConcept, status, authoredOn) |
| `vitals` | `Observation` — LOINC 8480-6/8462-4 (BP), 8867-4 (HR), 2339-0/2345-7 (glucose) |
| `last_encounter_date` | latest `Encounter.period.start` |

## Indexes
`name.family`, `gender`, `conditions.display`, `birthDate`

## Connection
Via `db/connection.py` — reads `MONGODB_URI` (default `mongodb://localhost:27017`),
retries the initial connect with backoff, enables retryable reads/writes.
