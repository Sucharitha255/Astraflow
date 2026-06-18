from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "astram_event_data.csv"

PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "processed_data.csv"