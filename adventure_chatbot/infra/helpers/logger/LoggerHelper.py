from typing import Any
import logging
import inspect
from adventure_chatbot.infra.helpers import ArgsHelper


class LoggerHelper:
    def __init__(self) -> None:
        self.argsHelper = ArgsHelper()
        self.args = self.argsHelper.getArgs()
        self.logLevel = self._getLogLevel(self.args.log_level)
        self.log_file = self.args.log_file
        self._getConfig()
        self.info(f"Logger initialized with log level {self.args.log_level}")

    def info(self, message: str, **kwargs: Any) -> None:
        functionName = self._getFunctionCallerName()
        log = self.logger.getLogger(functionName)
        log.info(message, extra=kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        functionName = self._getFunctionCallerName()
        log = self.logger.getLogger(functionName)
        log.error(message, extra=kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        functionName = self._getFunctionCallerName()
        log = self.logger.getLogger(functionName)
        log.warning(message, extra=kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        functionName = self._getFunctionCallerName()
        log = self.logger.getLogger(functionName)
        log.debug(message, extra=kwargs)

    def _getFunctionCallerName(self) -> str:
        functionCallerName = inspect.stack()[2].function
        classCallerName = inspect.stack()[2].filename.split("/")[-1].split(".")[0]
        return f"{classCallerName}.{functionCallerName}"

    def _getLogLevel(self, level: str) -> int:
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

    def _getConfig(self):
        self.logger = logging
        format = self._getTimestampFormat()
        format += "[ %(levelname)s ] "
        format += self._getClassNameFormat()
        format += "%(message)s"

        self.logger.basicConfig(
            format=format,
            level=self.logLevel,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def _getTimestampFormat(self) -> str:
        if self.logLevel == logging.DEBUG:
            return "%(asctime)s "
        return ""

    def _getClassNameFormat(self) -> str:
        if self.logLevel == logging.DEBUG:
            return "%(name)s "
        return ""