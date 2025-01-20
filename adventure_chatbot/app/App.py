from adventure_chatbot.app.chatbotDemo.ChatbotDemo import ChatbotDemoWindow
from adventure_chatbot.app.playground.Playground import PlaygroundWindow
from adventure_chatbot.app.settings.SettingsWindow import SettingsWindow
from adventure_chatbot.app.adventure.Adventure import AdventureWindow

import gradio as gr
class App:
    def __init__(self) -> None:
        pass

    def execute(self) -> gr.Blocks:
        screens: list[gr.Blocks] = []
        adventureWindow = AdventureWindow()
        adventure = adventureWindow.execute()
        screens.append(adventure)
        settingsWindow = SettingsWindow()
        settings = settingsWindow.execute()
        screens.append(settings)
        chatbotDemoWindow = ChatbotDemoWindow()
        chatbotDemo = chatbotDemoWindow.execute()
        screens.append(chatbotDemo)

        playgroudWindow = PlaygroundWindow(screens)
        playgroud = playgroudWindow.execute()

        with gr.Blocks(title="Adventure Chatbot") as adventure:
            playgroud.render()

        return adventure
