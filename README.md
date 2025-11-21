# 🤖 basic_chatbot  
A simple chatbot that uses **Google Gemini API** to answer user questions.  
I will be **constantly updating and improving** this project. 🚀

---

## ✨ Features
- ⚡ Uses **Gemini API**  
- 🌱 Beginner-friendly structure  
- 🔒 Secure API handling via `.env`  
- 🧩 Easy to extend and customize  
- 🔄 Continuous improvements planned  

---

## 📦 Tech Stack
- **Python**
- **FastAPI / Uvicorn**
- **Gemini API**
- **dotenv**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/basic_chatbot.git
cd basic_chatbot
###2️⃣ Create your .env file

Inside the backend/ folder, create a file named .env:

GEMINI_API_KEY=your_gemini_key_here

▶️ Running the Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

📂 Project Structure
basic_chatbot/
│
├── backend/
│   ├── main.py
│   ├── gemini_client.py
│   ├── schemas.py
│   ├── list_models.py
│   ├── requirements.txt
│   └── .env   (ignored)
│
├── frontend/
│   └── app.py
│
└── .gitignore

🛠️ Development Notes

This project is kept intentionally simple so beginners can understand:

How API requests work

How chatbots generate responses

How environment variables keep secrets safe

How backend and frontend connect


📈 Future Improvements

Planned updates include:

🌐 Add a proper frontend UI

💬 Conversation history

🧠 More advanced prompt engineering

🚀 Deploy the project online

🔒 Rate-limiting & API safety

📝 Logging

🤖 Support for multiple models
