from typing import Any
from reactpy import component, html

from adventure_chatbot.app.home.HomePage import HomePage

class HomeController:
    def __init__(self):
        self.page = HomePage()

    def index(self) -> Any:
        @component
        def HelloWorld():
            return self.page.page()
        
        return HelloWorld
    