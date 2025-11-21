from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load .env file BEFORE configuring Gemini
load_dotenv()

# Configure Gemini after loading key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_chat(model, messages):
    try:
        prompt = ""
        for msg in messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            prompt += f"{role}: {msg['content']}\n"

        model_client = genai.GenerativeModel(model)
        response = model_client.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "⚠️ No text returned from Gemini."

    except Exception as e:
        print("🔥 Gemini Error:", e)
        return f"❌ Gemini Error: {str(e)}"
