from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link

from lexicon import lexicon_ru
from keyboards import keyboards_greeting, keyboards_menu

router = Router()


@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(lexicon_ru.greeting_text.format(name=msg.from_user.full_name, link=f"{hide_link('https://i.ytimg.com/vi/nh0g83A7PKQ/maxresdefault.jpg')}"),
                     reply_markup=keyboards_greeting.kb_greeting)
    await msg.answer_sticker("CAACAgIAAxkBAAEBMmxlEbAmqpMTyGFsnzdlfpA67p1DLAACiysAApunuUpnYzvhbe6O7zAE", reply_markup=keyboards_menu.kb_menu)
