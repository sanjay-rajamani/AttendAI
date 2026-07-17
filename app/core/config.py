from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Settings:

    # ===============================
    # Application
    # ===============================
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    APP_ENV = os.getenv("APP_ENV")

    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    # ===============================
    # Database
    # ===============================
    DATABASE_TYPE = os.getenv("DATABASE_TYPE")
    DATABASE_URL = os.getenv("DATABASE_URL")

    # ===============================
    # Attendance Rules
    # ===============================
    MINIMUM_ATTENDANCE = int(os.getenv("MINIMUM_ATTENDANCE"))
    WARNING_ATTENDANCE = int(os.getenv("WARNING_ATTENDANCE"))
    SAFE_ATTENDANCE = int(os.getenv("SAFE_ATTENDANCE"))

    # ===============================
    # AI
    # ===============================
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # ===============================
    # Voice
    # ===============================
    WHISPER_MODEL = os.getenv("WHISPER_MODEL")

    # ===============================
    # WhatsApp
    # ===============================
    WHATSAPP_SESSION = os.getenv("WHATSAPP_SESSION")
    WHATSAPP_WEBHOOK = os.getenv("WHATSAPP_WEBHOOK")

    # ===============================
    # Timetable
    # ===============================
    DEFAULT_WORKING_DAYS = int(os.getenv("DEFAULT_WORKING_DAYS"))
    MAX_PERIODS_PER_DAY = int(os.getenv("MAX_PERIODS_PER_DAY"))

    # ===============================
    # Alerts
    # ===============================
    ENABLE_ALERTS = os.getenv("ENABLE_ALERTS") == "True"
    ALERT_TIME = os.getenv("ALERT_TIME")

    # ===============================
    # OCR
    # ===============================
    OCR_LANGUAGE = os.getenv("OCR_LANGUAGE")

    # ===============================
    # Logging
    # ===============================
    LOG_LEVEL = os.getenv("LOG_LEVEL")

    # ===============================
    # Timezone
    # ===============================
    TIMEZONE = os.getenv("TIMEZONE")

    # ===============================
    # Security
    # ===============================
    SECRET_KEY = os.getenv("SECRET_KEY")


settings = Settings()