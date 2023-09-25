from aiogram import Router, types
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link

from lexicon import lexicon_ru
from keyboards import keyboards_greeting

router = Router()


@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(lexicon_ru.greeting.format(name=msg.from_user.full_name, link=f"{hide_link('https://i.ytimg.com/vi/nh0g83A7PKQ/maxresdefault.jpg')}"),
                     reply_markup=keyboards_greeting.kb_greeting)
