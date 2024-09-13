import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Создание проекта"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK

    main_title = ft.Text("Ваши проекты", size=24)
    project_names = []
    data = []

    def create_project_name_fields(e: ft.ControlEvent):
        project_name_field = ft.TextField(label="Название проекта", autofocus=True, on_blur=lambda e: page.remove(
            project_name_field) if project_name_field.value == "" else None)
        project_names.append(project_name_field)
        page.controls.insert(len(page.controls) - 1, project_name_field)
        page.update()

    def save_names(e: ft.ControlEvent):
        global page_number, stack_page_flag, data_project_name, edit_stack_flag
        data_project_name = [project_name.value for project_name in project_names if project_name.value != ""]
        page_number = 0
        stack_page(e)
        stack_page_flag = True
        edit_stack_flag = False

    def stack_page(e: ft.ControlEvent, edit_stack=False):
        global page_number
        page.controls.clear()
        stack_fields = []
        page.add(ft.Text(f"Проект {data_project_name[page_number]}"))

        def add_stack(e: ft.ControlEvent, stack_value=None, version_value=None):
            # Создание двух текстовых полей
            stack = ft.TextField(label="Стек", width=200, value=stack_value)
            version = ft.TextField(label="Версия", width=200, value=version_value)

            # Создание строки с двумя текстовыми полями, выровненной по центру
            row = ft.Row(
                controls=[stack, version],
                alignment=ft.MainAxisAlignment.CENTER  # Выравнивание по центру
            )
            page.controls.insert(len(page.controls) - 1, row)
            stack_fields.append([stack, version])
            page.update()

        def save_stack(e: ft.ControlEvent):
            global page_number, edit_stack_flag
            data_stacks = []
            for i, j in stack_fields:
                data_stacks.append([i.value, j.value]) if not (i.value == j.value == "") else 0
            new_data = [data_project_name[page_number], data_stacks]

            if edit_stack_flag and not new_data in data:
                data[page_number] = new_data
            elif not new_data in data:
                data.append(new_data) if not new_data in data else 0
            if page_number < len(data_project_name) - 1:
                page_number += 1
                stack_page(e, edit_stack=edit_stack_flag)
            else:
                page_number = 0
                edit_stack_flag = True
                stack_page(e, edit_stack=edit_stack_flag)

        new_stack_btn = ft.ElevatedButton(text="Добавить стек", on_click=add_stack)
        page.add(new_stack_btn)
        page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT, on_click=save_stack)
        if edit_stack:
            for i, j in data[page_number][1]:
                add_stack(e, stack_value=i, version_value=j)

    new_project_btn = ft.ElevatedButton(text="Создать проект", on_click=create_project_name_fields)
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT, on_click=save_names)

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