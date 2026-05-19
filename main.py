from fastapi import FastAPI

from api.chat import router as chat_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Simple Ollama Chatbot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat_router)



@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def root():
    return {"message": "Chatbot API running"}