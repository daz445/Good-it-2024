from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
from aiogram.utils.keyboard import InlineKeyboardBuilder
async def main_keyboard():
    kb_list = [
        [KeyboardButton(text = "Добавить проект",web_app = WebAppInfo(url='https://bdu.fstec.ru/vul/2024-06792'))],
        [KeyboardButton(text = "Изменить проект")],
        [KeyboardButton(text = "Удалить проект")]
    ]
    kb = ReplyKeyboardMarkup(keyboard = kb_list, resize_keyboard=True,one_time_keyboard=True, input_field_placeholder="Воспользуйся меню")
    return kb



async def create_inline_keyboard():
    b = InlineKeyboardButton(text="Web", web_app='https://bdu.fstec.ru/vul/2024-06792') 
    kb = InlineKeyboardMarkup().add(b)
    return kb 