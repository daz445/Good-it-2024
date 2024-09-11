from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
from aiogram.fsm.storage.memory import MemoryStorage

ADMIN_ID = config('ADMIN_ID')
BOT_TOKEN = config("BOT_TOKEN")
HOST = config("HOST")
PORT = int(config("PORT"))
WEBHOOK_PATH = f'/{BOT_TOKEN}'
BASE_URL = config("BASE_URL")
#tgk_list = [{'label': 'Инфортех','url': 'https://t.me/infotecs_official'}]

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())