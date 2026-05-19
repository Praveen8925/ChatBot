from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are a helpful assistant.
Keep responses concise and directly answer the user.
If you are unsure, say you are unsure."""

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{message}"),
    ]
)