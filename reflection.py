import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def review_document(document):

    prompt = f"""
You are a Senior Technical Reviewer.

Review the following business document.

Check:

1. Missing sections
2. Grammar
3. Professional tone
4. Structure
5. Business quality
6. Completeness

If improvements are needed,
rewrite the document.

Return ONLY the improved document.

{document}
"""

    response = model.generate_content(prompt)

    return response.text