from os import PathLike
from typing import Optional
from settings import settings
from SimonsLogging.log_level import LogLevel
from SimonsLogging.log_message import LogMessage
from abc import ABC, abstractmethod
import os


class LoggingOutput(ABC):
    def __init__(self, log_level_override: Optional[LogLevel] = None):
        self.log_level_override: LogLevel = log_level_override

    def should_log(self, msg: LogMessage) -> bool:
        if settings.system.debug_mode:
            return True
        log_level = self.log_level_override
        if not log_level:
            log_level = settings.system.log_level
        if msg.level.value <= log_level:
            return True
        return False

    def log(self, msg: LogMessage):
        if self.should_log(msg):
            self._handle_log(msg)

    @abstractmethod
    def _handle_log(self, msg: LogMessage):
        raise NotImplementedError

    def _format_message(self, msg: LogMessage) -> str:
        return f"[{msg.level.name}] {msg.message}"