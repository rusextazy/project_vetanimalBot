from aiogram import Router, F
from aiogram.types import Message

from lexicon import lexicon_ru

router = Router()


@router.message(F.text == "🧬 Аптека")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_ru.pet_pharmacy_text)