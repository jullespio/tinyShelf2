from pathlib import Path
import json
from platformdirs import user_data_dir

APP_NAME = "tinyshelf2"
DATA_DIR = Path(user_data_dir(APP_NAME))
DATA_DIR.mkdir(parents=True, exist_ok=True)

LIBRARY_PATH = DATA_DIR / "library.json"

def load_library():
    if LIBRARY_PATH.exists():
        with open(LIBRARY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_library(data):
    with open(LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
