from adventure_chatbot.infra.http import Routes
from fastapi import FastAPI
import uvicorn

class ServerHttp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.router = Routes()
        self.app = FastAPI()
    
    def start(self) -> None:
        self.router.execute(self.app)
        uvicorn.run(self.app, host=self.host, port=self.port)
    
    def reload(self) -> FastAPI:
        self.router.execute(self.app)
        return self.app