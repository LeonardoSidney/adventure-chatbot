import gradio as gr
import pandas as pd

from adventure_chatbot import SettingsController, SettingsServices

class SettingsWindow:
    def __init__(self) -> None:
        self.controller = SettingsController()
        self.service = SettingsServices()

    def execute(self):
        self.foldersConfig: list[dict[str, str]] = self.controller.getFoldersName()
        foldersName: list[str] = self.service.getFoldersName(self.foldersConfig)
        foldersLocation: list[str] = self.service.getFoldersLocation(self.foldersConfig)
        self.foldersLayout: dict[str, list[str]] = self.service.getFoldersLayout(
            self.foldersConfig
        )
        print("Folders name: ", foldersName)
        print("Folders layout: ", self.foldersLayout)
        with gr.Blocks(title="Settingsss") as settingsWindow:
            gr.Interface(fn=self.getFoldersLayout, inputs=None, outputs=gr.Dataframe(),flagging_mode="never")

            gr.Dropdown(
                foldersName,
                label="Models folders",
                info="Folders where the models are stored",
                interactive=True,
            )
            gr.Dropdown(
                foldersLocation,
                label="Besast",
                info="Will add more animals later!",
                interactive=True,
            )
            # gr.DataFrame(
            #     headers=["Name", "Location"],
            #     datatype=["str", "str"],
            #     value=self.services.getFoldersLayout(self.foldersConfig),
            #     inputs=self._foldersDataframeInput(),
            # )

        return settingsWindow

    def getFoldersLayout(self):
        return pd.DataFrame(self.foldersLayout)
