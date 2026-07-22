import json

from app.ai.gemini_service import ask_gemini


def parse_intent(message: str):

    response = ask_gemini(message)

    print("\n========== GEMINI RESPONSE ==========")
    print(response)
    print("=====================================\n")

    try:
        return json.loads(response)

    except Exception:
        return {
            "intent": "unknown",
            "raw_response": response
        }