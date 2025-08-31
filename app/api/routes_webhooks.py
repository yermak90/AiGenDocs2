from fastapi import APIRouter, Request, Response, status
from aiogram import Bot, Dispatcher
from app.core.config import settings

router = APIRouter()

def telegram_path() -> str:
    # секрет в пути
    return f"/tg/webhook/{settings.TG_WEBHOOK_SECRET}"

@router.post(telegram_path())
async def telegram_webhook(request: Request) -> Response:
    bot = request.app.state.bot
    dp: Dispatcher = request.app.state.dp
    data = await request.json()
    await dp.feed_webhook_update(bot, data)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/oauth/google/callback")
async def google_callback():
    return {"status":"ok"}
