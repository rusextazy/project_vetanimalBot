from aiogram import Router, F
from aiogram.types import Message

from lexicon import lexicon_pet_supplies, lexicon_ru

router = Router()


@router.message(F.text == "🦮 Товары для собак")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_pet_supplies.dog_text)


@router.message(F.text == "🐈 Товары для кошек")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_pet_supplies.cat_text)


@router.message(F.text == "🐹 Товары для грызунов")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_pet_supplies.rodents_text)


@router.message(F.text == "🧬 Аптека")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_ru.pet_pharmacy_text)
    await msg.answer(text=lexicon_pet_supplies.pharmacy_text)
