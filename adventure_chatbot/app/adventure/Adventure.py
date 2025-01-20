import gradio as gr

class AdventureWindow:
    def __init__(self) -> None:
        pass

    def execute(self) -> gr.Blocks:
        with gr.Blocks(title="Adventure") as adventureWindow:
            textArea = gr.TextArea()
            textArea.label = "Adventure"
            submitButton = gr.Button()
            submitButton.value = "Submit"
            submitButton.variant = "primary"
            submitButton.click(self.submitClickButton, inputs=textArea, outputs=textArea)
            
        return adventureWindow
    
    def submitClickButton(self, text: str) -> str:
        return text + "You clicked the button\n"

