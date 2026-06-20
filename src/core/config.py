import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = ROOT / "config"

SETTINGS_FILE = CONFIG_DIR / "settings.json"
PERMISSIONS_FILE = CONFIG_DIR / "permissions.json"


class Config:

    def __init__(self):

        self.settings = self.load_json(
            SETTINGS_FILE
        )

        self.permissions = self.load_json(
            PERMISSIONS_FILE
        )

    def load_json(self, path):

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_setting(self, key, default=None):

        return self.settings.get(key, default)

    def get_permission(self, key, default=False):

        return self.permissions.get(key, default)