from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from decouple import config 
from utils.db import get_user_by_id, add_user, get_projects_by_id
from aiogram.types import Message, CallbackQuery
from keyboards import keybords_users as us_kb   

# from keyboards.keybords_users import main_contact_kb, channels_kb

router = Router()



# функция для реагирования на команду /start
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(config('Welcome_Text'), reply_markup=us_kb.main_keyboard())
    telegram_id = message.from_user.id
    user_data = await get_user_by_id(telegram_id)
    if user_data is None:
        # Если пользователь не найден, добавляем его в базу данных
        await add_user(
            telegram_id=telegram_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
        inGroupe = True
    else:
        # Получаем статус bot_open для пользователя
        inGroupe = user_data.get('inGroupe', False)  # Второй параметр по умолчанию False

    if not inGroupe:
        # Если пользователь подписался на все каналы
        await message.answer("Тут основная логика бота, чуть позже напишем")
    else:
        pass
        # Иначе показываем клавиатуру с каналами для подписки
        # await message.answer(
        #     "Для пользования ботом необходимо подписаться на следующие каналы:",
        #     reply_markup=channels_tgk(kb_list))



    


# функция для реагирования на команду /мои проекты
@router.message(Command('myprojects'))
async def command_myproject_handler(message: Message) -> None:
    await message.answer(f"Ваши проекты:{get_projects_by_id(message.from_user.id)}")


# функция для реагирования на команду /помщь
@router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer("Помогите")







#Реакция на сообщение канала
@router.channel_post()
async def chanel_message(chanel: Message):
    await chanel.answer(chanel.text.split("\n")[0]+'\n'+
    chanel.text.split("\n")[2]+'\n'+
    chanel.text.split("\n")[3])

    