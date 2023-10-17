from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import keyboards_menu
from lexicon import lexicon_ru


router = Router()


@router.message(F.text == "🔙 Главное меню")
@router.message(F.text == "Отмена")
@router.message(F.text == "Меню")
async def main_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=keyboards_menu.kb_menu)


@router.message(F.text == "📌 Зоотовары")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_ru.pet_supplies_text, reply_markup=keyboards_menu.kb_menu_product)


@router.message(F.text == "📞 Контакты")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_ru.contacts_text)


@router.message(F.text == "💰 Price")
async def replenish(msg: Message):
    await msg.answer(text=lexicon_ru.price_text)
