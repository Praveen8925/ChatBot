from fastapi import APIRouter, HTTPException

from schema.chat import ChatRequest, ChatResponse
from llm.client import build_chat_chain

router = APIRouter(tags=["chat"])

chatbot, model = build_chat_chain()


@router.get("/health")
async def health():
    try:
        # Simple ping to model
        await chatbot.ainvoke({"message": "hi"})

        return {
            "status": "ok",
            "model": model,
            "llm": "connected"
        }

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"LLM unavailable: {e}"
        )


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    try:
        reply = await chatbot.ainvoke(
            {"message": req.message},
            config={"configurable": {"session_id": req.session_id}}
        )

        return ChatResponse(
            reply=reply,
            model=model
        )

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"LLM unavailable: {e}"
        )
@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):

    try:

        reply = await chatbot.ainvoke(

            {"message": req.message},

            config={
                "configurable": {
                    "session_id": req.session_id
                }
            }
        )

        return ChatResponse(
            reply=reply,
            model=model
        )

    except Exception as e:

        raise HTTPException(
            status_code=503,
            detail=str(e)
        )