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
        cursor = await db.execute(f"SELECT name FROM Projects WHERE telegram_id = {telegram_id}")
        rows = await cursor.fetchall()

        if rows is None:
            return None

        projs = []
        for row in rows:
            projs.append(row[0])
        
        return projs
    
async def get_all_users_by_attack_stack(words:str):
    async with aiosqlite.connect("main.db") as db:
        ans = []
 
        for word in words.split(" "):
            
            cursor = await db.execute(f"SELECT telegram_id FROM Stack WHERE stack LIKE '%{word.lower()}%'")
            find = await cursor.fetchall()
            if find:
                ans += find
    return list(set([x[0] for x in ans]))


async def isInproject(telegram_id: int, name: str):
    async with aiosqlite.connect("main.db") as db:
        cursor =  await db.execute(f"SELECT * FROM Projects WHERE telegram_id = '{telegram_id}' & name = '{name}'")
        rows = await cursor.fetchall()

        if rows is None:
            return False
        return True




# Добавление проекта пользователя
async def add_project(telegram_id: int, name: str)->None:
    async with aiosqlite.connect("main.db") as db:
        print(await isInproject(telegram_id,name))
        if not(await isInproject(telegram_id,name)):
            await db.execute("""
            INSERT INTO Projects (telegram_id, name)
            VALUES (?, ?)
        """, (telegram_id, name))
            await db.commit()











'''



def edit_iq(ids: str, IQ:int) ->None:
  users_iq=list(map(lambda x:x[1],all_users_list))
  users_ids = list(map(lambda x:x[0],all_users_list))
  cursor.execute(f"UPDATE USERS SET 'IQ' = '{users_iq[users_ids.index(ids)] + IQ}' WHERE id = '{ids}' ")
  conn.commit()


def deleat(base: str,par: str, val)->None:
	cursor.execute(f'DELETE FROM {base} WHERE {par} = "{val}"')
	conn.commit()

'''

        


    