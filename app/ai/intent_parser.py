import json

from app.ai.local_intent import parse_local_intent
from app.ai.gemini_service import ask_gemini


def parse_intent(message: str):
    """
    Parse user intent.

    Priority:
    1. Local Intent Engine
    2. Gemini AI (fallback)
    """

    # -----------------------
    # Local Intent
    # -----------------------
    local_intent = parse_local_intent(message)

    if local_intent is not None:

        print("\n========== LOCAL INTENT ==========")
        print(local_intent)
        print("==================================\n")

        return local_intent

    # -----------------------
    # Gemini Fallback
    # -----------------------
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