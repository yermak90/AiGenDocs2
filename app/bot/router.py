from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from .states import RegStates
from .keyboards import home_kb, confirm_inline_kb

router = Router(name="tg")

@router.message(F.text.in_({"/start", "🏠 Домой"}))
async def cmd_start(m: Message, state: FSMContext):
    await state.clear()
    await m.answer("Добро пожаловать! Выберите действие:", reply_markup=home_kb())

@router.message(F.text == "🧾 Регистрация / Профиль")
async def reg_entry(m: Message, state: FSMContext):
    await state.set_state(RegStates.upload_id)
    await m.answer("Шаг 1: загрузите удостоверение (фото/PDF).", reply_markup=home_kb())

@router.message(RegStates.upload_id, F.document | F.photo)
async def reg_ocr(m: Message, state: FSMContext):
    # TODO: скачать файл, OCR → ФИО/ИИН/сроки
    await m.answer("Распознал данные. Проверьте и подтвердите.", reply_markup=None)
    await m.answer("Подтверждаем?", reply_markup=confirm_inline_kb())

@router.callback_query(F.data.startswith("confirm:"))
async def confirm(cb: CallbackQuery, state: FSMContext):
    action = cb.data.split(":")[1]
    if action == "ok":
        await state.set_state(RegStates.phone)
        await cb.message.answer("Шаг 2: Введите телефон БЕЗ +7 и 8 (10 цифр).")
    elif action == "retry":
        await state.set_state(RegStates.upload_id)
        await cb.message.answer("Загрузите файл ещё раз.")
    else:
        await state.clear()
        await cb.message.answer("Отменено.", reply_markup=home_kb())
    await cb.answer()

@router.message(RegStates.phone, F.text.regexp(r"^\d{10}$"))
async def reg_phone_ok(m: Message, state: FSMContext):
    # сохранить phone
    await state.set_state(RegStates.moderation)
    await m.answer("Шаг 3: Модерация заявки. Мы уведомим вас в Telegram после проверки.")

# Пример обработчика меню «📝 Создать договор»
@router.message(F.text == "📝 Создать договор")
async def create_contract(m: Message):
    await m.answer("Выберите контрагента или пришлите файл с реквизитами для OCR.")
