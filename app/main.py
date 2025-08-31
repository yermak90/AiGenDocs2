import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from app.core.config import settings
from app.api.routes_public import router as public_router
from app.api.routes_webhooks import router as webhooks_router, telegram_path
from app.bot.router import router as bot_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)
    app.include_router(public_router)
    app.include_router(webhooks_router)
    return app

app = create_app()

@app.on_event("startup")
async def on_startup():
    # Telegram
    bot = Bot(token=settings.TG_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    dp.include_router(bot_router)
    app.state.bot = bot
    app.state.dp = dp
    # Webhook
    webhook_url = settings.PUBLIC_BASE_URL.rstrip("/") + telegram_path()
    await bot.set_webhook(webhook_url)
    # TODO: APScheduler init for reminders

@app.on_event("shutdown")
async def on_shutdown():
    await app.state.bot.session.close()
