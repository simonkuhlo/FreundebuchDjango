from simons_logging.log_message import LogMessage
from .abstract_logging_output import LoggingOutput

class SimplePrintOutput(LoggingOutput):
    def _handle_log(self, msg: LogMessage):
        print(self._format_message(msg))