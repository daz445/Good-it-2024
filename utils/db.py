import aiosqlite


# Добавляем пользователя
async def add_user(telegram_id: int, username: str, first_name: str):
    async with aiosqlite.connect("main.db") as db:
        await db.execute("""
            INSERT INTO users (telegram_id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO NOTHING
        """, (telegram_id, username, first_name))
        await db.commit()

# Получаем всех пользователей
async def get_all_users():
    async with aiosqlite.connect("main.db") as db:
        cursor = await db.execute("SELECT * FROM Users")
        rows = await cursor.fetchall()

        # Преобразуем результаты в список словарей
        users = [
            {
                "telegram_id": row[0],
                "username": row[1],
                "first_name": row[2],
                "inGroupe": bool(row[3])
            }
            for row in rows
        ]
        return users


async def get_user_by_id(telegram_id: int):
    async with aiosqlite.connect("main.db") as db:
        cursor = await db.execute("SELECT * FROM Users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()

        if row is None:
            return None

        # Преобразуем результат в словарь
        user = {
            "telegram_id": row[0],
            "username": row[1],
            "first_name": row[2],
            "inGroupe": bool(row[3])
        }
        return user
    
async def get_projects_by_id(telegram_id: int):
    async with aiosqlite.connect("main.db") as db:
        cursor = await db.execute("SELECT name FROM Projects WHERE telegram_id = ?", (telegram_id,))
        rows = await cursor.fetchone()

        if rows is None:
            return None

        projs = []
        for row in rows:
            projs.append(row[0])
        
        return projs
    
async def update_bot_open_status(telegram_id: int, bot_open: bool):
    async with aiosqlite.connect("main.db") as db:
        await db.execute("""
            UPDATE Users
            SET inGroupe = ?
            WHERE telegram_id = ?
        """, (bot_open, telegram_id))
        await db.commit()