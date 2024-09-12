import flet as ft
from create_bot import BASE_URL_FOR_APP

def main(page: ft.Page) -> None:
    # await asyncio.sleep(1)
    page.title = "Создание проекта"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Поля для ввода
    project_name_input = ft.TextField(label="Название проекта", autofocus=True)
    stack_input = ft.TextField(label="Стек проекта")

    # Обработчик нажатия кнопки
    def on_save_click(e):
        project_name = project_name_input.value
        stack = stack_input.value
        page.add(ft.Text(f"Проект '{project_name}' со стеком '{stack}' сохранен!", color=ft.colors.GREEN))

    # Кнопка "Сохранить"
    save_button = ft.ElevatedButton("Сохранить", on_click=on_save_click)

    # Добавление элементов на страницу
    page.add(
        project_name_input,
        stack_input,
        save_button
    )

def start_app():
    print("App_start")
    ft.app(target=main, name="add_project",port=8080,view=None)
