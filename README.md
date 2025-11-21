# 🤖 basic_chatbot  
A simple and beginner-friendly chatbot that uses **Google Gemini API** to answer user questions.  
I will be **constantly updating and improving** this project over time. 🚀

---

## ✨ Features
- ⚡ Uses **Gemini API** to generate responses  
- 🧩 Basic and easy-to-understand code structure  
- 🌱 Beginner-friendly project for learning how chatbots work  
- 🔒 Secure API usage via environment variables  
- 🔧 Backend built with Python (FastAPI or similar – adjust as needed)  
- 🔄 Continuous improvements planned  

---

## 📦 Tech Stack
- **Python**  
- **Gemini API (Google AI)**  
- **FastAPI / Uvicorn**  
- **dotenv for environment variables**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/basic_chatbot.git
cd basic_chatbot

### 2️⃣ Create your .env file
```bash
Create a file named .env in the backend folder:

GEMINI_API_KEY=your_gemini_key_here

### ▶️ Running the Backend
```bash
If your backend uses FastAPI + Uvicorn (adjust if different):

cd backend
pip install -r requirements.txt
uvicorn main:app --reload
---
🛠️ Development Notes

This project is kept intentionally simple so beginners can understand how:

API requests work

Chatbots generate responses

Environment variables are used securely

The backend and frontend connect
---
📈 Future Improvements

Planned upgrades include:

🌐 Add a proper frontend UI

💬 Conversation history

🧠 More advanced prompt engineering

🚀 Deploy the project online

🔒 Add rate-limit & API safety checks

📝 Add logging

🤖 Add multiple model support
