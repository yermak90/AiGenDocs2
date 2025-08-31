from aiogram.fsm.state import StatesGroup, State

class RegStates(StatesGroup):
    upload_id = State()
    phone = State()
    moderation = State()
    google = State()
    done = State()
