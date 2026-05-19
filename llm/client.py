import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history  import Runnable
from langchain_core.runnables.history import RunnableWithMessageHistory


from langchain_core.chat_history import InMemoryChatMessageHistory

# Preferred modern package:
from langchain_ollama import ChatOllama

from llm.prompt import chat_prompt

store = {}


def get_session_history(session_id: str):

    if session_id not in store:

        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


def build_chat_chain() -> tuple[Runnable, str]:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "gemma4:e2b")

    llm = ChatOllama(
        base_url=base_url,
        model=model,
        temperature=0.2,
    )

    chain = chat_prompt | llm | StrOutputParser()

    chatbot = RunnableWithMessageHistory(

        chain,

        get_session_history,

        input_messages_key="message",
    )
    return chatbot, model

