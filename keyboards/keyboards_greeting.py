from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

kb_greeting = [
    [InlineKeyboardButton(text="Самая лучшая милашка", url="https://t.me/spectropfobia"),
     InlineKeyboardButton(text="Муж милашки", url="https://t.me/rusextaz")],
    [InlineKeyboardButton(text="Канал милашек", url="https://t.me/tyt_rus")]
]

kb_greeting = types.InlineKeyboardMarkup(inline_keyboard=kb_greeting)