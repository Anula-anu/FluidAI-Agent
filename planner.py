import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def create_plan(user_request):

    prompt = f"""
You are an autonomous AI planning agent.

User Request:
{user_request}

Generate:

1. Objective
2. Assumptions
3. TODO List
4. Execution Steps

Return in Markdown.
"""

    response = model.generate_content(prompt)

    return response.text