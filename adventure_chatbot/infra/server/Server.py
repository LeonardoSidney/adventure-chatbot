from fastapi import FastAPI
from adventure_chatbot.infra.http import ServerHttp

class Server:
    def __init__(self, args):
        self.args = args

    def execute(self):
        self.http = self._startHttpServer()

    def _startHttpServer(self):
        server = ServerHttp(self.args.host, self.args.port)
        return server.execute()