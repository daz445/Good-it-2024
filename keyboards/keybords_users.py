from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, Repl
from decouple import config
def main_keyboard():
    kb_list = [
        [KeyboardButton(text = "Добавить проект",web_app = WebAppInfo(url='https://bdu.fstec.ru/vul/2024-06792'))],
        [KeyboardButton(text = "Изменить проект")],
        [KeyboardButton(text = "Удалить проект")]
    ]
    kb = ReplyKeyboardMarkup(keyboard = kb_list, resize_keyboard=True,one_time_keyboard=True, input_field_placeholder="Воспользуйся меню")
    return kb



def

