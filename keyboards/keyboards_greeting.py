from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

kb_greeting = [
    [InlineKeyboardButton(text="Милашка", url="https://t.me/spectropfobia"),
     InlineKeyboardButton(text="Муж милашки", url="https://t.me/rusextaz")],
    [InlineKeyboardButton(text="Канал милашек", url="https://t.me/+1OWfWFlFiBxjMjky")]
]

kb_greeting = types.InlineKeyboardMarkup(inline_keyboard=kb_greeting)