import chainlit as cl


@cl.on_chat_start
def main():
    if res := cl.AskUserMessage(
        content="What is your name?", timeout=10
    ).send():
        cl.Message(
            content=f"Your name is: {res['content']}",
        ).send()
