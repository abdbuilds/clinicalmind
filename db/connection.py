"""
MongoDB connection helper for ClinicalMind — secure, with retry.

- Connection string comes from the MONGODB_URI env var (never hard-coded), so
  the same code works for local MongoDB and for an authenticated/TLS Atlas URI.
- Retries the initial connection with exponential backoff.
- Enables driver-level retryable reads/writes.

Usage:
    from db.connection import get_collection
    patients = get_collection("patients")
"""

import logging
import os
import time

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

log = logging.getLogger(__name__)

# Config from environment (local default). For Atlas set e.g.:
#   MONGODB_URI="mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true&tls=true"
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.environ.get("MONGODB_DB", "clinicalmind")

_client: MongoClient | None = None


def get_client(max_retries: int = 5, base_delay: float = 1.0) -> MongoClient:
    """Return a shared MongoClient, retrying the initial connection."""
    global _client
    if _client is not None:
        return _client

    last_err: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            client = MongoClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=3000,  # fail fast if server is down
                connectTimeoutMS=3000,
                retryWrites=True,               # driver retries transient write errors
                retryReads=True,                # ...and reads
                appname="clinicalmind",
            )
            client.admin.command("ping")        # force a real round-trip
            log.info("Connected to MongoDB on attempt %d", attempt)
            _client = client
            return client
        except (ConnectionFailure, ServerSelectionTimeoutError) as err:
            last_err = err
            delay = base_delay * (2 ** (attempt - 1))
            log.warning(
                "MongoDB connect failed (attempt %d/%d): %s — retrying in %.1fs",
                attempt, max_retries, err, delay,
            )
            time.sleep(delay)

    raise ConnectionError(
        f"Could not connect to MongoDB at {MONGODB_URI} after {max_retries} attempts"
    ) from last_err


def get_db(name: str | None = None):
    return get_client()[name or MONGODB_DB]


def get_collection(name: str, db_name: str | None = None):
    return get_db(db_name)[name]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db = get_db()
    print(f"✅ Connected to '{db.name}'. Collections: {db.list_collection_names()}")
