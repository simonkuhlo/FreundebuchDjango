from typing import List
from .logger import Logger
from .logging_output import SimpleFileOutput, SimplePrintOutput, LoggingOutput

outputs: List[LoggingOutput] = [SimpleFileOutput(), SimplePrintOutput()]
default_logger = Logger(outputs)