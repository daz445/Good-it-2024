from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from decouple import config 
from utils.db import get_user_by_id, add_user, get_projects_by_id
from aiogram.types import Message
from keyboards import keybords_users as us_kb   
from create_bot import bot
from utils import db, utils


# from keyboards.keybords_users import main_contact_kb, channels_kb

router = Router()


# функция для реагирования на команду /start
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text =  '''Добро пожаловать в бета-верисю телаграм бота для оповещения пользователей о возникновении новых CVE 💻\n 
                          \nБот создан в рамках хакатона, организованным Itгородом 🦄\n
                          \nКейс от компании Infotecs\n
                          \nДля получение дополнительной информации⚙️ - /help ''', reply_markup=await us_kb.main_keyboard())
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
        #await message.answer("Тут основная логика бота, чуть позже напишем")
        pass
    else:
        pass
        # Иначе показываем клавиатуру с каналами для подписки
        # await message.answer(
        #     "Для пользования ботом необходимо подписаться на следующие каналы:",
        #     reply_markup=channels_tgk(kb_list))



    


# функция для реагирования на команду /мои проекты
@router.message(Command('myprojects'))
async def command_myproject_handler(message: Message) -> None:
    projects = await get_projects_by_id(message.from_user.id)
    if projects:
        text = "Ваши проекты:"
        for x in projects:
            text += '\n'+x
    else:
        text = "У вас нет проектов"
    await message.answer(text=text)



# функция для реагирования на команду /помщь
@router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer(text ="""Посмотреть свои проекты - /myprojects\n
                         \nДобавить проект - первая кнопка\n
                         \nБот, использует miniapps 📲\n
                         \nОстальные функции будут доступны чуть позже ⏳""")
    

# Рассылка сообщений пользователю
@router.channel_post()
async def chanel_cmd(chanel:Message):
    t = chanel.text
    users = await db.get_all_users_by_attack_stack(str(await utils.text_editor(t)).lower())
    print(users)
    for user in users:
        url = await utils.url_editor(t)
        await bot.send_message(chat_id=user,
                               text= "Выявлена новая уязвимость",reply_markup= await us_kb.channels_kb(url))
            