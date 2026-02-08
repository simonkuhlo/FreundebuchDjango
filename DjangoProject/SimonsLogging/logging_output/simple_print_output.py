from SimonsLogging.log_message import LogMessage
from .logging_output import LoggingOutput

class SimplePrintOutput(LoggingOutput):
    def _handle_log(self, msg: LogMessage):
        print(self._format_message(msg))