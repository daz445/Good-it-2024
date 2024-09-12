import logging
from aiogram.types import BotCommand, BotCommandScopeDefault, ReplyKeyboardMarkup
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from create_bot import bot, dp, BASE_URL, WEBHOOK_PATH, HOST, PORT, ADMIN_ID
from handlers.user_handlers import router
from handlers.admin_handlers import router as admin_router
from utils.utils import cheack_chanel
import asyncio
from web_app import start_app
import multiprocessing

async def set_commands():
    # Создаем список команд, которые будут доступны пользователям
    commands = [
                BotCommand(command='start', description='Старт'),
                BotCommand(command='myprojects', description='Мои проекты'),
                BotCommand(command='help', description='Помогите')
                ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())



# Функция, которая будет вызвана при запуске бота
async def on_startup() -> None:
    # Устанавливаем командное меню
    await set_commands()
    # Устанавливаем вебхук для приема сообщений через заданный URL
    await bot.set_webhook(f"{BASE_URL}{WEBHOOK_PATH}")
    # Отправляем сообщение администратору о том, что бот был запущен
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен!')



# Функция, которая будет вызвана при остановке бота
async def on_shutdown() -> None:
    # Отправляем сообщение администратору о том, что бот был остановлен
    await bot.send_message(chat_id=ADMIN_ID, text='Бот остановлен!')
    # Удаляем вебхук и, при необходимости, очищаем ожидающие обновления
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Закрываем сессию бота, освобождая ресурсы
    await bot.session.close()




# Основная функция, которая запускает приложение
def main() -> None:
    
    
    # Подключаем маршрутизатор (роутер) для обработки сообщений
    dp.include_router(router)
    dp.include_router(admin_router)

    # Регистрируем функцию, которая будет вызвана при старте бота
    dp.startup.register(on_startup)

    # Регистрируем функцию, которая будет вызвана при остановке бота
    dp.shutdown.register(on_shutdown)
    
    # Создаем веб-приложение на базе aiohttp
    app = web.Application()

    # Настраиваем обработчик запросов для работы с вебхуком
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,  # Передаем диспетчер
        bot=bot  # Передаем объект бота

    )
    # Регистрируем обработчик запросов на определенном пути
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Настраиваем приложение и связываем его с диспетчером и ботом
    setup_application(app, dp, bot=bot)

    # Запускаем веб-сервер на указанном хосте и порте
    web.run_app(app, host=HOST, port=PORT)
    

# Точка входа в программу
if __name__ == "__main__":
    
    # asyncio.run(
    # main()
        # )
    
    process1 = multiprocessing.Process(target=main)
    process1.start()
    # with Pool(processes=4) as pool:
    #     pool.map(start_app,main)
    process2 = multiprocessing.Process(target=start_app)
    process2.start()
    # await start_app()
    #process2.join()
    

    # Ждем завершения процессов
    # process2.join()
    # process1.join()
    
    
    # Настраиваем логирование (информация, предупреждения, ошибки) и выводим их в консоль
    
    # Запускаем основную функцию



