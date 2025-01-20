import argparse

class ArgsHelper:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._define_args()
        self.args = self.parser.parse_args()

    def get_args(self) -> argparse.Namespace:
        return self.args
    
    def _define_args(self):
        self.parser.add_argument("--dummy_arg", help="Reload the server", action="store_true")