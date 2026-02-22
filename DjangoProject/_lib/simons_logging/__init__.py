from typing import List
from .logger import Logger
from .logging_output import SimpleFileOutput, SimplePrintOutput, LoggingOutput
from _lib.settings import settings

file_output: SimpleFileOutput = SimpleFileOutput(
    log_level_override=settings.logging.file.log_level_override,
    log_file_path=settings.logging.file.file_path,
    file_name=settings.logging.file.file_name
)

console_output: SimplePrintOutput = SimplePrintOutput(
    log_level_override=settings.logging.console.log_level_override
)

outputs: List[LoggingOutput] = [file_output, console_output]
default_logger = Logger(outputs)