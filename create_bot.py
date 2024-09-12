from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
from aiogram.fsm.storage.memory import MemoryStorage
from telethon import TelegramClient
from fastapi import FastAPI, Request

ADMIN_ID = config('ADMIN_ID')
BOT_TOKEN = config("BOT_TOKEN")
HOST = config("HOST")
PORT = int(config("PORT"))
WEBHOOK_PATH = f'/{BOT_TOKEN}'
BASE_URL = config("BASE_URL")
API_ID = config("API_ID")
API_HASH = config("API_HASH")
channel_username = 'bdufstecru'  # юзернейм канала (без @)
# NGROK =  "https://2feb-46-30-36-215.ngrok-free.app"

#tgk_list = [{'label': 'Инфортех','url': 'https://t.me/infotecs_official'}]

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


# Создаем экземпляр клиента
client = TelegramClient("MyVisit",API_ID,API_HASH)