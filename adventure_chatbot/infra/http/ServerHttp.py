from adventure_chatbot.infra.http import Routes
from fastapi import FastAPI
import uvicorn

class ServerHttp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.router = Routes()
        self.app = FastAPI()

    def execute(self) -> FastAPI:
        self.router.execute(self.app)
        return self.app
        