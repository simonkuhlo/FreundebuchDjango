# config.py
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
import json

BASE_DIR = Path(__file__).resolve().parent

class NetworkSettings(BaseModel):
    # TODO NOT IMPLEMENTED
    host: str = Field(default="127.0.0.1") # The used hostname
    # TODO NOT IMPLEMENTED
    port: int = Field(default=8000, ge=1, le=65535) # The used port

class SystemSettings(BaseModel):
    debug_mode: bool = Field(default=True)
    log_level: int = Field(default=0)
    language_code: str = Field(default="en-us")
    timezone: str = Field(default="UTC")

class UserSettings(BaseModel):
    max_entries: int = Field(default=1) # -1 = no limit
    #TODO NOT IMPLEMENTED
    code_overrides_limit: bool = Field(default=False) # If enabled, users can use creation codes to exceed their maximum number of entries

class EntriesSettings(BaseModel):
    # TODO NOT IMPLEMENTED
    creation_is_protected: bool = Field(default=True) # If enabled, only logged in users or creation codes can create new entries

class BaseLoggingOutputSettings(BaseModel):
    active: bool = Field(default=True)
    log_level_override: Optional[int] = Field(default=None)

class ConsoleLoggingSettings(BaseLoggingOutputSettings):
    pass

class DatabaseLoggingSettings(BaseLoggingOutputSettings):
    pass

class FileLoggingSettings(BaseLoggingOutputSettings):
    file_path: str = Field(default="")
    file_name: str = Field(default="log.txt")

class LoggingSettings(BaseModel):
    level: int = Field(default=0)
    console: ConsoleLoggingSettings = ConsoleLoggingSettings()
    file: FileLoggingSettings = FileLoggingSettings()
    database: DatabaseLoggingSettings = DatabaseLoggingSettings()

class Settings(BaseModel):
    network: NetworkSettings = NetworkSettings()
    system: SystemSettings = SystemSettings()
    user: UserSettings = UserSettings()
    logging: LoggingSettings = LoggingSettings()

    @classmethod
    def from_json(cls, path: Path) -> "Settings":
        with path.open() as f:
            data = json.load(f)
        return cls(**data)

settings = Settings.from_json(BASE_DIR / "settings.json")

if __name__ == "__main__":
    print(settings)
