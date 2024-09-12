from aiogram.enums import ContentType, ChatMemberStatus
from create_bot import bot, client, channel_username
from typing import Any, List




async def cheack_chanel():
    # Подключаемся к клиенту
    
    await client.start()

    # Получаем сообщения из канала
    async for message in client.iter_messages(channel_username, limit=4):
        
        print(message.sender_id, message.text)




async def is_user_subscribed(channel_url: str, telegram_id: int) -> bool:
    try:
        # Получаем username канала из URL
        channel_username = channel_url.split('/')[-1]

        # Получаем информацию о пользователе в канале
        member = await bot.get_chat_member(chat_id=f"@{channel_username}", user_id=telegram_id)

        # Проверяем статус пользователя
        if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]:
            return True
        else:
            return False
    except Exception as e:
        # Если возникла ошибка (например, пользователь не найден или бот не имеет доступа к каналу)
        print(f"Ошибка при проверке подписки: {e}")
        return False


async def text_editor(t) -> str:
    source = t.split('\n')
    block_text = source[0]
    return  block_text
async def url_editor(t):
    source = t.split('\n')
    block_url = source[2]
    return block_url
      









