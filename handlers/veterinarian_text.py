from contextlib import suppress
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.markdown import hide_link

from keyboards import keyboards_doctor
from lexicon import lexicon_doctor


router = Router()

smiles = [
    [f"{hide_link('https://i.imgur.com/FttzTxh.jpg')}", lexicon_doctor.mineeva],
    [f"{hide_link('https://i.imgur.com/NyarDJM.jpg')}", lexicon_doctor.alekseeva],
    [f"{hide_link('https://i.imgur.com/rJKmhh8.jpg')}", lexicon_doctor.kolodyazhina]
]


@router.callback_query(keyboards_doctor.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: keyboards_doctor.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{smiles[page][0]}{smiles[page][1]}",
            reply_markup=keyboards_doctor.paginator(page)
        )
    await call.answer()


@router.message(F.text == "💊 Врачи")
async def replenish(msg: Message):
    await msg.answer(text="В нашем вет.центре \"Алия\" на данный момент 3 специалиста:")
    await msg.answer(text=f"{smiles[0][0]}{smiles[0][1]}", reply_markup=keyboards_doctor.paginator())