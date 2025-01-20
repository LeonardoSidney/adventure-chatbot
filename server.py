from argparse import Namespace

import gradio as gr
from adventure_chatbot import Main, ArgsHelper

def start_gradio() -> gr.Blocks:
    main = Main()
    adventure = main.startApp()
    return adventure


def start_console():
    main = Main()
    main.execute()

def start_server(args: Namespace):
    # start_gradio()
    start_console()
    
if __name__ == "__main__":
    argsHelper = ArgsHelper()
    args = argsHelper.get_args()
    start_server(args)
    # adventure = start_gradio()
    # with gr.Blocks() as demo:
    #     adventure.render()
    # demo.launch()