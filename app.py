import streamlit as st
from utils.LLM import generate_response
from utils.prompts import get_question_prompt, greeting

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="TalentScout Assistant", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #0E1117;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🤖 TalentScout Hiring Assistant")
st.markdown("### *AI-powered candidate screening system*")

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = "start"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📋 Candidate Info")

    if "name" in st.session_state:
        st.write(f"👤 {st.session_state.name}")
    if "email" in st.session_state:
        st.write(f"📧 {st.session_state.email}")
    if "phone" in st.session_state:
        st.write(f"📱 {st.session_state.phone}")
    if "exp" in st.session_state:
        st.write(f"💼 {st.session_state.exp} years")
    if "position" in st.session_state:
        st.write(f"🎯 {st.session_state.position}")

# ---------------- PROGRESS BAR ----------------
progress_map = {
    "start": 0,
    "name": 10,
    "email": 20,
    "phone": 30,
    "experience": 50,
    "position": 60,
    "location": 70,
    "tech_stack": 85,
    "end": 100
}

st.progress(progress_map.get(st.session_state.step, 0))

# ---------------- WELCOME ----------------
if st.session_state.step == "start" and not st.session_state.messages:
    st.info("👋 Welcome! I’ll guide you through a quick hiring screening process.")

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Type your response...")

# Exit button
if st.button("❌ End Conversation"):
    st.session_state.messages.append(("assistant", "Thank you! Goodbye."))
    st.stop()

# ---------------- LOGIC ----------------
if user_input:
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.messages.append(("assistant", "Thank you! Goodbye."))
        st.stop()

    st.session_state.messages.append(("user", user_input))

    step = st.session_state.step

    if step == "start":
        bot_reply = greeting()
        st.session_state.step = "name"

    elif step == "name":
        st.session_state.name = user_input
        bot_reply = "📧 Could you please share your email address?"
        st.session_state.step = "email"

    elif step == "email":
        st.session_state.email = user_input
        bot_reply = "📱 Please enter your phone number."
        st.session_state.step = "phone"

    elif step == "phone":
        st.session_state.phone = user_input
        bot_reply = "💼 How many years of experience do you have?"
        st.session_state.step = "experience"

    elif step == "experience":
        st.session_state.exp = user_input
        bot_reply = "🎯 What position are you applying for?"
        st.session_state.step = "position"

    elif step == "position":
        st.session_state.position = user_input
        bot_reply = "📍 What is your current location?"
        st.session_state.step = "location"

    elif step == "location":
        st.session_state.location = user_input
        bot_reply = "🧠 Enter your tech stack (e.g. Python, React, SQL):"
        st.session_state.step = "tech_stack"

    elif step == "tech_stack":
        st.session_state.tech_stack = user_input

        prompt = get_question_prompt(user_input)
        questions = generate_response(prompt)

        bot_reply = f"""
### 🧠 Technical Assessment

Here are your interview questions:

{questions}
"""
        st.session_state.step = "end"

    elif step == "end":
        bot_reply = "✅ Thank you! Our team will review your responses and contact you soon."

    else:
        bot_reply = "⚠️ Something went wrong. Please restart."

    st.session_state.messages.append(("assistant", bot_reply))

# ---------------- DISPLAY CHAT ----------------
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)