import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Создание проекта"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.theme_mode = ft.ThemeMode.DARK

    main_title = ft.Text("Ваши проекты", size=24)
    project_names = []

    def create_project_name_fields(e: ft.ControlEvent):
        project_name_field = ft.TextField(label="Название проекта", autofocus=True, on_blur=lambda e: page.remove(
            project_name_field) if project_name_field.value == "" else None)
        project_names.append(project_name_field)
        page.add(project_name_field)

    def edit_page(e: ft.ControlEvent):
        page.controls.clear()
        page.add(
            ft.Text("project"),
            ft.Row(
                [
                    ft.Column(spacing=0, controls=[ft.TextField(label="Name") for i in range(10)]),
                    ft.Column(spacing=0, controls=[ft.TextField(label="Version") for i in range(10)]),
                ],
                spacing=0,
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    new_project_btn = ft.ElevatedButton(text="Создать проект", on_click=create_project_name_fields)
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT, on_click=edit_page)

    page.add(
        main_title,
        new_project_btn,
    )


def start_app():
    print("App_start")
    ft.app(target=main, name="add_project",port=8080,view=None)





""" 
import flet as ft 
from create_bot import BASE_URL_FOR_APP

def main(page: ft.Page) -> None:
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

"""