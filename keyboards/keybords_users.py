from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
from web_app import start_app
from create_bot import BASE_URL_FOR_APP
async def main_keyboard():
    kb_list = [
        [KeyboardButton(text = "Добавить проект",web_app = WebAppInfo(url=f'{BASE_URL_FOR_APP}/add_project/'))],
        [KeyboardButton(text = "🐻 Выгрузить проекты с GitFlic")]
    ]
    kb = ReplyKeyboardMarkup(keyboard = kb_list, resize_keyboard=True,one_time_keyboard=True, input_field_placeholder="Нажми меню")
    return kb



async def channels_kb(code:str):
    inline_keyboard = []
    inline_keyboard.append(
        [InlineKeyboardButton(
            text="Подробнее", 
            web_app=WebAppInfo(
                url='https://bdu.fstec.ru/vul/'+str(code).replace('BDU:','')
                               )
                               )
                               ]
                               )
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def check_data():
    kb_list = [
        [InlineKeyboardButton(text="✅Да, все верно.", callback_data='correct')],
        [InlineKeyboardButton(text="🔙Я поменяю имя пользователя", callback_data='incorrect')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb_list)