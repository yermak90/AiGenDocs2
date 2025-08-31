from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главная (HOME) — повторяем структуру из дерева
def home_kb() -> ReplyKeyboardMarkup:
    rows = [
        [KeyboardButton(text="🧾 Регистрация / Профиль"), KeyboardButton(text="📝 Создать договор")],
        [KeyboardButton(text="📄 Счёт на оплату"), KeyboardButton(text="🧾 АВР и АОУ")],
        [KeyboardButton(text="📑 Счёт-фактура"), KeyboardButton(text="📂 Просмотреть документы")],
        [KeyboardButton(text="📊 Аналитика"), KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="🚪 Выйти")],
    ]
    # Анти-тупики
    rows.append([KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Домой"), KeyboardButton(text="✖️ Отмена")])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)

def confirm_inline_kb(ok="✅ Подтвердить", retry="🔁 Загрузить снова", cancel="✖️ Отмена") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=ok, callback_data="confirm:ok"),
        InlineKeyboardButton(text=retry, callback_data="confirm:retry"),
        InlineKeyboardButton(text=cancel, callback_data="confirm:cancel"),
    ]])
