def get_question_prompt(tech_stack):
    return f"""
You are a senior technical interviewer at a top tech company.

Generate 3-5 high-quality interview questions based on:

Tech Stack: {tech_stack}

Requirements:
- Focus on real-world scenarios
- Include at least one problem-solving question
- Mix beginner to intermediate level
- Keep questions clear and concise
"""

def greeting():
    return """
👋 Hello! Welcome to TalentScout Hiring Assistant.

I will guide you through a quick screening process.
Let's get started!

👉 What is your full name?
"""

def fallback():
    return "⚠️ Sorry, I didn’t understand that. Could you please clarify?"