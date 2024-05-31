import flet as ft
import re
from models.client import post_client
from user_controls.alert_dialog import AlertDialog
from user_controls.app_nav import nav_view


def ClientsRegisterView(page: ft.Page, id_client=None):
    # NAVIGATION
    nav: ft.Column = nav_view(page) 
    alert = AlertDialog(page)

    # -- CONTROLS --
    text_id_client    = ft.Text(value=id_client)

    text_name    = ft.TextField(label='Nombre', width=500, border='UNDERLINE', text_size=17)
    text_phone   = ft.TextField(label="Phone", text_align=ft.TextAlign.LEFT, width=500, border='UNDERLINE', text_size=16, input_filter=ft.NumbersOnlyInputFilter(), max_length=10)
    text_email   = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=500, border='UNDERLINE', text_size=16)
    text_address = ft.TextField(label='Dirección', width=500, border='UNDERLINE', text_size=16)

    
    btn_cancel = ft.ElevatedButton('Cancelar', color=ft.colors.WHITE, on_click=lambda e: cancel(e), bgcolor=ft.colors.RED)
    btn_register = ft.ElevatedButton('Agregar', color=ft.colors.WHITE, on_click=lambda e: add_client(e), bgcolor=ft.colors.GREEN)

    # -- FUNCTIONS --
    def is_valid_email(email):
        regex = r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$'
        if re.match(regex, email):
            return True
        return False

    def add_client(e: ft.ControlEvent):
        if not validate_inputs():
            alert.show(title="Error", content="Todos los campos son requeridos", status="error")
            clean_fields()
            return
        if not is_valid_email(text_email.value):
            alert.show(title="Advertencia", content="Correo invalido", status="warning")
            clean_fields()
            return
        post_client(text_name.value, text_phone.value, text_email.value, text_address.value)
        alert.show(title="Éxito", content="Producto registrado", status="success")
        page.go('/clients')


    def cancel(e: ft.ControlEvent):
        page.go('/clients')
    
    def validate_inputs():
        if all([text_name.value, text_phone, text_email, text_address]):
            return True
        return False
    
    def clean_fields():
        text_name.value = ''
        text_phone.value = ''
        text_email.value = ''
        text_address.value = ''
        page.update()


    # -- EVENTS --
    text_name.on_change = validate_inputs
    text_phone.on_change = validate_inputs
    text_email.on_change = validate_inputs
    text_address.on_change = validate_inputs



    # -- CONTENT --
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.RED, on_click=lambda e: page.go('/clients'))
                ],
                width=500,
                alignment=ft.MainAxisAlignment.END
            ),
            ft.Text("Registrar Cliente", size=20),
            text_name,
            text_phone,
            text_email,
            text_address,
            ft.Row(
                [
                    btn_cancel,
                    btn_register
                ],
                alignment=ft.MainAxisAlignment.END,
                width=500
            )
        ],
        width=1400,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    view = ft.Container(
        content=ft.Row(
            controls=[
                nav, 
                content
            ], 
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )
    
    
    return view

