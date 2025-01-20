from enum import Enum

class EnumMessagesPrefix(Enum):
    INFO = "[INFO]"
    WARNING = "[WARNING]"
    ERROR = "[ERROR]"

class EnumColorMessages(Enum):
    INFO = "\033[1;32;40m"
    WARNING = "\033[1;33;40m"
    ERROR = "\033[1;31;40m"
    