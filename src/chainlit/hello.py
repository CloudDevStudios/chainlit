# This is a simple example of a chainlit app.

from chainlit import AskUserMessage, Message, on_chat_start


@on_chat_start
def main():
    if res := AskUserMessage(content="What is your name?", timeout=30).send():
        Message(
            content=f"Your name is: {res['content']}.\nChainlit installation is working!\nYou can now start building your own chainlit apps!",
        ).send()
