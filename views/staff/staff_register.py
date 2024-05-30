import flet as ft
import re
from models.staff import addStaff, get_staff_by_id, update_staff
from user_controls.alert_dialog import AlertDialog


def is_valid_email(email):
    regex = r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$'
    if re.match(regex, email):
        return True
    return False

def registerStaffView(page, id:int=None):

    # Controls 
    text_name  :ft.TextField = ft.TextField(label="Nombres", text_align=ft.TextAlign.LEFT, width=500, border='underline')
    text_last_name  :ft.TextField = ft.TextField(label="Apellidos", text_align=ft.TextAlign.LEFT, width=500, border='underline')
    text_phone :ft.TextField = ft.TextField(label="Phone", text_align=ft.TextAlign.LEFT, width=500, input_filter=ft.NumbersOnlyInputFilter(), max_length=10, border='underline')
    text_email :ft.TextField = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=500, border='underline')
    dwn_area = ft.Dropdown(label='Área', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=500, border='underline', text_size=15,
                        options=[
                                ft.dropdown.Option("admin"),
                                ft.dropdown.Option("compras"),
                                ft.dropdown.Option("ventas"),
                                ft.dropdown.Option("envios"),
                                ft.dropdown.Option("transportista"),
                            ])
    text_passw :ft.TextField = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=500, password=True, can_reveal_password=True, max_length=8, border='underline')
    btn_save = ft.ElevatedButton("Guardar", width=500, disabled=True)
    alert_dialog = AlertDialog(page)
    

    # Functions
    def registerStaff(e):
        if is_valid_email(text_email.value):
            addStaff(text_name.value, text_last_name.value, text_phone.value, text_email.value, dwn_area.value, text_passw.value)
            alert_dialog.show(title="ÉXITO", content="Usuario registrado", status="success")
            # page.go('/staff')
        else:
            alert_dialog.show(title="ERROR", content="Correo o Contraseña incorrectos", status="error")
            print('click')

    def updateStaff(e):
        if is_valid_email(text_email.value):
            update_staff(id,text_name.value, text_last_name.value, text_phone.value, text_email.value, dwn_area.value, text_passw.value)
            alert_dialog.show(title="ÉXITO", content="Usuario Actualizado", status="success")
        else:
            alert_dialog.show(title="ERROR", content="Correo o Contraseña incorrectos", status="error")
            print('click')

    def validateInputs(e):
        if all([text_name.value, text_last_name, text_phone.value, text_email.value, dwn_area.value, text_passw.value]):
            btn_save.disabled = False
        else:
            btn_save.disabled = True
        page.update()    


    # Events
    btn_save.on_click = registerStaff
    text_name.on_change  = validateInputs
    text_last_name.on_change  = validateInputs
    text_phone.on_change = validateInputs
    text_email.on_change = validateInputs
    dwn_area.on_change  = validateInputs
    text_passw.on_change = validateInputs


    if id != None:
        data = get_staff_by_id(id)
        for staff in data:
            text_name.value = staff.sta_name
            text_last_name.value = staff.sta_last_name
            text_phone.value = staff.sta_phone
            text_email.value = staff.sta_email
            dwn_area.value = staff.sta_area
            text_passw.value = staff.sta_password
            btn_save.label = "Actualizar"
            btn_save.disabled = False
            btn_save.on_click = updateStaff
        page.update()


    content = ft.Row(
        [
            ft.Column([
                ft.Text("Registrar Trabajador", size=20),                
                text_name,
                text_last_name,
                text_phone,
                text_email,
                dwn_area,
                text_passw,
                btn_save
            ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )       

            
    return content