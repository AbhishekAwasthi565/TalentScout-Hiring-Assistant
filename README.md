#  TalentScout Hiring Assistant

An AI-powered Hiring Assistant chatbot designed to streamline the initial candidate screening process for **TalentScout**, a fictional recruitment agency specializing in technology placements.

This application leverages **Large Language Models (LLaMA 3.1 via Groq API)** and an interactive **Streamlit UI** to collect candidate information and generate tailored technical interview questions based on their tech stack.

---

##  Features

###  Intelligent Candidate Screening

* Collects essential candidate details:

  * Full Name
  * Email Address
  * Phone Number
  * Years of Experience
  * Desired Position
  * Current Location
  * Tech Stack

---

###  Dynamic Technical Question Generation

* Generates **3–5 personalized technical questions**
* Questions are:

  * Context-aware
  * Based on declared tech stack
  * Mixed difficulty (beginner → intermediate)
  * Real-world oriented

---

###  Conversational AI Experience

* Maintains **context across conversation**
* Provides **natural and structured dialogue flow**
* Handles:

  * Greeting
  * Follow-ups
  * Exit conditions

---

###  Enhanced User Interface

* Built with **Streamlit**
* Features:

  * Chat-based interaction
  * Sidebar candidate dashboard
  * Progress tracking bar
  * Clean and responsive UI

---

###  Fallback Handling

* Handles invalid or unclear inputs gracefully
* Keeps conversation aligned with hiring purpose

---

##  Project Architecture

```bash
TalentScout-Chatbot/
│── app.py                # Main Streamlit app
│── requirements.txt      # Dependencies
│── .env                  # API keys (not committed)
│
└── utils/
    │── llm.py            # LLM integration (Groq API)
    │── prompts.py        # Prompt engineering logic
```

---

##  Tech Stack

| Component       | Technology Used      |
| --------------- | -------------------- |
| Frontend UI     | Streamlit            |
| Backend Logic   | Python               |
| LLM             | LLaMA 3.1 (Groq API) |
| Environment     | python-dotenv        |
| Version Control | Git                  |

---

##  Prompt Engineering Strategy

### 🔹 Information Gathering

Prompts are designed to:

* Be **clear and structured**
* Guide users step-by-step
* Maintain conversational tone

---

### 🔹 Technical Question Generation

Dynamic prompt template:

```
You are a senior technical interviewer.

Generate 3-5 high-quality interview questions based on:

Tech Stack: {user_input}

Requirements:
- Real-world scenario based
- Include problem-solving question
- Mix difficulty levels
```

---

### 🔹 Context Handling

* Uses session state to track:

  * Conversation stage
  * User responses
* Ensures **logical progression of interaction**

---

##  Data Privacy & Handling

* No real user data is stored permanently
* Uses **in-memory session state only**
* API keys are stored securely using `.env`
* Designed with **privacy-first approach**

---

##  Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd TalentScout-Chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

##  Usage Guide

1. Launch the app
2. Chatbot greets you
3. Provide requested details step-by-step
4. Enter your tech stack
5. Receive AI-generated technical questions
6. End conversation

---

##  Challenges & Solutions

### ❌ Challenge: Model Deprecation

* Initial model (`llama3-70b-8192`) was deprecated

✅ Solution:

* Migrated to **latest model: `llama-3.1-70b-versatile`**

---

### ❌ Challenge: Conversation Flow Management

* Maintaining structured interaction

✅ Solution:

* Implemented **state-based flow using Streamlit session state**

---

### ❌ Challenge: Dynamic Question Generation

* Handling diverse tech stacks

✅ Solution:

* Designed **flexible prompt templates** adaptable to any tech stack

---

##  Future Improvements

*  Candidate scoring system
*  AI-based answer evaluation
*  Multilingual support
*  Sentiment analysis
*  Cloud deployment (AWS / GCP)

---

##  Demo

*(Add Loom / video link here)*

---

##  Conclusion

This project demonstrates:

* Practical use of **LLMs in real-world applications**
* Strong **prompt engineering skills**
* Ability to build **end-to-end AI systems**
* Focus on **user experience and scalability**

---

##  Author

**Abhishek Awasthi**
AI/ML Enthusiast | Python Developer

---
