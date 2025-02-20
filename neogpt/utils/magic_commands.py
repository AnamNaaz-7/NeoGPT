from rich.console import Console
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory

console = Console()
cprint = lambda *args, **kwargs: console.print(*args, **kwargs)
# This file contains the magic commands that can be used during chat sessions.

def magic_commands(user_input,chain):
    
    if user_input == f"/reset":
        cprint("Resetting the chat session...")
        print(chain.combine_documents_chain.memory)
        chain.combine_documents_chain.memory.chat_memory = ChatMessageHistory(messages=[])
        print(chain.combine_documents_chain.memory.chat_memory)
        return True

    elif user_input == f"/exit":
        cprint("\nNeoGPT 🤖 is shutting down. Bye 👋")
        return False

    else:
        cprint("Invalid command. Please try again.")


# Uncomment the following lines to test the magic commands
# if __name__ == "__main__":
#     magic_commands("/exit")