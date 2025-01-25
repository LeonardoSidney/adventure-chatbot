import argparse

class ArgsHelper:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._defineArgs()
        self.args = self.parser.parse_known_args()[0]

    def getArgs(self) -> argparse.Namespace:
        return self.args
    
    def _defineArgs(self):
        self.parser.add_argument("--reload", help="Run in reload mode, please use uvicorn server:app", action="store_true", default=False)
        self.parser.add_argument("--port", help="Port to run the server", type=int, default=8000)
        self.parser.add_argument("--host", help="Host to run the server", type=str, default="localhost")
        self.parser.add_argument("--log_level", help="Log level", type=str, default="DEBUG")
        self.parser.add_argument("--log_file", help="Log file", type=str, required=False)