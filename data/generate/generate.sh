#!/usr/bin/env bash
#
# generate.sh — reproducibly generate synthetic FHIR patients with Synthea and
# load them into MongoDB (ClinicalMind, Day 6).
#
# Usage:
#   ./data/generate/generate.sh [count]      # default 1000
#
set -euo pipefail

COUNT="${1:-1000}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SYNTHEA_DIR="$ROOT/synthea"
JAR="$SYNTHEA_DIR/synthea.jar"
JAR_URL="https://github.com/synthetichealth/synthea/releases/download/master-branch-latest/synthea-with-dependencies.jar"

# Java 17 (installed via Homebrew, keg-only)
export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"

mkdir -p "$SYNTHEA_DIR"

if [ ! -f "$JAR" ]; then
  echo "Downloading Synthea (~90MB)..."
  curl -L -sS -o "$JAR" "$JAR_URL"
fi

echo "Generating $COUNT synthetic FHIR patients..."
( cd "$SYNTHEA_DIR" && java -jar synthea.jar -p "$COUNT" \
    --exporter.baseDirectory=./output --exporter.fhir.export=true )

echo "Loading patients into MongoDB..."
"$ROOT/.venv/bin/python" "$ROOT/scripts/load_patients_to_mongo.py"

echo "Done. Browse clinicalmind.patients in MongoDB Compass (mongodb://localhost:27017)."
