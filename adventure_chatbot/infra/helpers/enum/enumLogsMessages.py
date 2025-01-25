from enum import Enum

class EnumColorMessages(str, Enum):
    INFO = "\x1b[22m\x1b[32m"
    DEBUG = "\x1b[1m\x1b[36m"
    WARNING = "\x1b[1m\x1b[33m"
    ERROR = "\x1b[1m\x1b[31m"
    