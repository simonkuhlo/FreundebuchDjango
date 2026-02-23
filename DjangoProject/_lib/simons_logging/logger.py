from typing import List
from .log_level import LogLevel
from .logging_output import AbstractLoggingOutput
from .log_message import LogMessage

class Logger:
    def __init__(self, outputs: List[AbstractLoggingOutput]):
        self.outputs: List[AbstractLoggingOutput] = outputs

    def log(self, msg:LogMessage):
        for output in self.outputs:
            output.log(msg)

    def log_debug(self, content: str):
        message: LogMessage = LogMessage(level=LogLevel.DEBUG, message=content)
        self.log(message)

    def log_info(self, content: str):
        message: LogMessage = LogMessage(level=LogLevel.INFO, message=content)
        self.log(message)

    def log_warning(self, content: str):
        message: LogMessage = LogMessage(level=LogLevel.WARNING, message=content)
        self.log(message)

    def log_error(self, content: str):
        message: LogMessage = LogMessage(level=LogLevel.ERROR, message=content)
        self.log(message)