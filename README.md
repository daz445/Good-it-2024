[![infotecs](https://edu.mascom-vostok.ru/wp-content/uploads/2022/01/infoteks.png?branch=master)](https://infotecs.ru/?ysclid=m0xf80t9bv289047031)


# 🛡️ Система отслеживания уязвимостей в компонентах ПО

Добро пожаловать в проект **Система отслеживания уязвимостей**! Этот проект создан для того, чтобы своевременно информировать пользователей о новых уязвимостях в их программных стеках и предоставить удобный инструмент для их отслеживания.

## 📋 Задачи проекта

1. **Создание современного Telegram-бота** 🤖, который способен эффективно выполнять свои функции по отслеживанию и оповещению.
2. **Своевременное оповещение** ⏰ пользователей о появлении новых уязвимостей в их компонентах ПО.
3. **Интеграция mini-apps** 📱 в Telegram-бота для комфортного и интуитивного взаимодействия пользователей с ботом.

## 🚀 Стек технологий

Проект основан на использовании следующих технологий:

- **Python 3.10** 🐍 - основной язык разработки
- **Aiohttp 3.10.5** 🌐 - асинхронная библиотека для работы с HTTP
- **FastAPI 0.114.0** ⚡ - фреймворк для создания веб-приложений
- **Aiogram 3.12.0** 💬 - фреймворк для работы с Telegram API
- **SQLite** 🗄️ - легковесная и эффективная СУБД для хранения данных
- **Aiosqlite 0.20.0** 🔄 - библиотека для асинхронной работы с SQLite

## 🛠️ Особенности

### База данных и соединения

- В проекте используется **SQLite**, что позволяет эффективно создавать и управлять сложными запросами с минимальными затратами ресурсов.
- Благодаря использованию технологии **webhook**, бот моментально отправляет и получает информацию, не прибегая к прямому взаимодействию с серверами Telegram. Это делает систему быстрой и отзывчивой ⚡.

### Webhooks и mini-apps

Для работы с webhooks и mini-apps в проекте использовался сервис **nGrok** 🌐. Он позволяет создать локальный сервер с доступом в интернет, что упрощает разработку и развертывание.

## 📐 Архитектура проекта

- Проект спроектирован с использованием **микросервисной архитектуры** 🧩, что позволяет легко вносить изменения в отдельные компоненты системы.
- Поддерживается **многопроцессорный режим** 🖥️, что гарантирует стабильную работу даже при возникновении ошибок в разных частях проекта.
- Бот способен обрабатывать сообщения как от **отдельных пользователей** 👤, так и от **групп и каналов** 💬.

### Mini-apps

Реализованы удобные и интуитивные **mini-apps** 📱, которые позволяют пользователю легко взаимодействовать с ботом, получать информацию о последних уязвимостях и настраивать бота под свои нужды.

---

## 💻 Запуск проекта

Чтобы развернуть и запустить проект на локальной машине, выполните следующие шаги:

1. Склонируйте репозиторий:
   ```bash
   git clone <url>
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Настройте webhook с помощью **nGrok**:
   ```bash
   ngrok http <ваш порт>
   ```

4. Запустите бота:
   ```bash
   python main.py
   ```

---

## 🙌 Благодарности

Спасибо всем органтзаторам, наставникам и другим участникам за чудесный опыт участия в хакаоне