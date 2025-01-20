import random
import time
import gradio as gr


class ChatbotDemoWindow:
    def __init__(self) -> None:
        pass

    def execute(self) -> gr.Blocks:
        with gr.Blocks(title="chatbot") as chatbotWindow:
            chatbot = gr.Chatbot(type="messages")
            msg = gr.Textbox()
            clear = gr.Button("Clear")

            def user(user_message, history: list):
                return "", history + [{"role": "user", "content": user_message}]

            def bot(history: list):
                bot_message = random.choice(
                    ["How are you?", "I love you", "I'm very hungry"]
                )
                history.append({"role": "assistant", "content": ""})
                for character in bot_message:
                    history[-1]["content"] += character
                    time.sleep(0.05)
                    yield history

            msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
                bot, chatbot, chatbot
            )
            clear.click(lambda: None, None, chatbot, queue=False)
        return chatbotWindow
