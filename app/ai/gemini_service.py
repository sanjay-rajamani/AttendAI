from google import genai

from app.core.config import settings
from app.ai.prompt import SYSTEM_PROMPT


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def ask_gemini(user_message: str):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_message}
"""

    try:

        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("\n========== GEMINI ERROR ==========")
        print(e)
        print("==================================\n")

        return """
{
    "intent":"error",
    "message":"Gemini API unavailable"
}
"""