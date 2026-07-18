from google import genai

from app.core.config import settings
from app.ai.prompt import SYSTEM_PROMPT

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_gemini(user_message: str):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_message}
"""

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt
    )

    return response.text