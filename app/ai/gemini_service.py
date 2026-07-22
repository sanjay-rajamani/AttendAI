import time

from google import genai

from app.ai.prompt import SYSTEM_PROMPT
from app.core.config import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def ask_gemini(user_message: str):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_message}
"""

    retries = 3
    delay = 2

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt
            )

            print("\n========== GEMINI RESPONSE ==========")
            print(response.text)
            print("=====================================\n")

            return response.text

        except Exception as e:

            print("\n========== GEMINI ERROR ==========")
            print(e)
            print("==================================\n")

            if attempt < retries - 1:

                print(f"Retrying in {delay} seconds...\n")
                time.sleep(delay)
                delay *= 2

            else:

                return """
{
    "intent":"error",
    "message":"Gemini API unavailable"
}
"""