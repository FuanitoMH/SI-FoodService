import flet as ft
import re
from models.staff import addStaff
from user_controls.alert_dialog import AlertDialog


def is_valid_email(email):
    regex = r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$'
    if re.match(regex, email):
        return True
    return False

def registerStaffView(page):
    
    # Controls 
    text_name  :ft.TextField = ft.TextField(label="Nombres", text_align=ft.TextAlign.LEFT, width=300)
    text_last_name  :ft.TextField = ft.TextField(label="Apellidos", text_align=ft.TextAlign.LEFT, width=300)
    text_phone :ft.TextField = ft.TextField(label="Phone", text_align=ft.TextAlign.LEFT, width=300, input_filter=ft.NumbersOnlyInputFilter(), max_length=10, )
    text_email :ft.TextField = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=300)
    text_rool  :ft.TextField = ft.TextField(label="Rool", text_align=ft.TextAlign.LEFT, width=300)
    text_passw :ft.TextField = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=300, password=True, can_reveal_password=True, max_length=8)
    btn_register = ft.ElevatedButton("Registrar", width=300, disabled=True)
    alert_dialog = AlertDialog(page)
    

    # Functions
    def registerStaff(e):
        if is_valid_email(text_email.value):
            addStaff(text_name.value, text_last_name.value, text_phone.value, text_email.value, text_rool.value, text_passw.value)
            alert_dialog.show(title="SUCCESS", content="Usuario registrado", status="success")
            page.go('/login')
        else:
            alert_dialog.show(title="ERROR", content="Correo o Contraseña incorrectos", status="error")
            print('click')


    def validateInputs(e):
        if all([text_name.value, text_last_name, text_phone.value, text_email.value, text_rool.value, text_passw.value]):
            btn_register.disabled = False
        else:
            btn_register.disabled = True
        page.update()


    # Events
    btn_register.on_click = registerStaff
    text_name.on_change  = validateInputs
    text_last_name.on_change  = validateInputs
    text_phone.on_change = validateInputs
    text_email.on_change = validateInputs
    text_rool.on_change  = validateInputs
    text_passw.on_change = validateInputs


    content = ft.Row(
        [
            ft.Column([
                ft.Text("Registrate", size=20),                
                text_name,
                text_last_name,
                text_phone,
                text_email,
                text_rool,
                text_passw,
                btn_register
            ])
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )       

            
    return content