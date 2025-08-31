from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Base
    APP_NAME: str = "SmartBudgetBuddy"
    ENV: str = "prod"
    PUBLIC_BASE_URL: str  # https://<your-railway-domain>
    SECRET_KEY: str

    # DB
    DATABASE_URL: str  # postgresql+asyncpg://user:pass@host:port/db

    # Telegram
    TG_BOT_TOKEN: str
    TG_WEBHOOK_SECRET: str = "tg-webhook"   # часть пути
    TG_ADMIN_IDS: str = ""  # "123,456"

    # Google
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str  # f"{PUBLIC_BASE_URL}/oauth/google/callback"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

settings = Settings()
