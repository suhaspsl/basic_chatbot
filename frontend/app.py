import streamlit as st
import requests

st.title("💬 My Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display existing messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input (Streamlit's built-in chat UI)
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to chat
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        # Send request to backend
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"messages": st.session_state["messages"]},
            timeout=60
        )

        # Parse JSON safely
        data = response.json()

        # Expected response from backend: {"reply": "..."}
        ai_message = data.get("reply")

        if not ai_message:
            ai_message = "⚠️ Backend response format error"

    except requests.exceptions.JSONDecodeError:
        ai_message = f"❌ Backend did not return JSON.\n\nResponse was:\n{response.text}"

    except Exception as e:
        ai_message = f"❌ Error while contacting backend:\n{str(e)}"

    # Add assistant message
    st.session_state["messages"].append({"role": "assistant", "content": ai_message})
    st.chat_message("assistant").write(ai_message)
