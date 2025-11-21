from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os
from gemini_client import generate_chat

load_dotenv()

print("Loaded GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-pro-latest"



class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

app = FastAPI()

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        messages_history = [msg.dict() for msg in req.messages]
        ai_reply = generate_chat(MODEL, messages_history)

        if not isinstance(ai_reply, str):
            ai_reply = str(ai_reply)

        return {"reply": ai_reply}

    except Exception as e:
        print("🔥 Backend Error:", str(e))  # LOG TO TERMINAL
        return {"reply": f"❌ Server Error: {str(e)}"}
