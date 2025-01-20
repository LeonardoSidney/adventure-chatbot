import gradio as gr
from adventure_chatbot import Main

if __name__ == "__main__":
    main = Main()
    adventure = main.startApp()
    with gr.Blocks() as demo:
        adventure.render()
    demo.launch()