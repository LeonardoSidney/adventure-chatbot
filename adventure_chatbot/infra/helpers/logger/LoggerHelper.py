from typing import Any
import logging
import inspect


class LoggerHelper:
    def __init__(self, level: str = "WARNING", logToFile: bool = False) -> None:
        self.logging = logging
        self.logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.level = self._setLoggerLevel(level)

    def info(self, message: str, **kwargs: Any) -> None:
        functionCallerName = inspect.stack()[1].function
        classCallerName = inspect.stack()[1].filename.split("/")[-1].split(".")[0]
        logName = f"{classCallerName}.{functionCallerName}"
        log = self.logging.getLogger(logName)
        log.info(message, extra=kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        functionCallerName = inspect.stack()[1].function
        classCallerName = inspect.stack()[1].filename.split("/")[-1].split(".")[0]
        logName = f"{classCallerName}.{functionCallerName}"
        log = self.logging.getLogger(logName)
        log.error(message, extra=kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        functionCallerName = inspect.stack()[1].function
        classCallerName = inspect.stack()[1].filename.split("/")[-1].split(".")[0]
        logName = f"{classCallerName}.{functionCallerName}"
        log = self.logging.getLogger(logName)
        log.warning(message, extra=kwargs)

    def _setLoggerLevel(self, level: str) -> int:
        if level == "DEBUG":
            return logging.DEBUG
        if level == "INFO":
            return logging.INFO
        if level == "WARNING":
            return logging.WARNING
        if level == "ERROR":
            return logging.ERROR
        if level == "CRITICAL":
            return logging.CRITICAL
        return logging.INFO
