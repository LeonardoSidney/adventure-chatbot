import gradio as gr
type tabs = list[gr.Blocks]

class PlaygroundWindow:
    def __init__(self, tabs: tabs) -> None:
        self.tabs = tabs
        pass

    def execute(self) -> gr.Blocks:
        with gr.Blocks() as layout:
            for tab in self.tabs:
                with gr.Tab(tab.title):
                    tab.render()
        return layout
