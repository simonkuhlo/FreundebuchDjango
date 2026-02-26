# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path
from _lib.settings import Settings

BASE_DIR = Path(__file__).resolve().parent.parent

instance_settings = Settings.from_json(path = BASE_DIR / "./config/settings_dev.json")