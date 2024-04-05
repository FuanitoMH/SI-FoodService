import flet as ft
from models.staff import addStaff

def registerStaffView(page):
    
    name = ft.TextField(label="Nombre", value='juan', text_align=ft.TextAlign.RIGHT, width=100)
    phone = ft.TextField(label="Phone", text_align=ft.TextAlign.RIGHT, width=100)
    email = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=100)
    rool = ft.TextField(label="Rool", text_align=ft.TextAlign.LEFT, width=100)
    pw = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=100)
    
   
    def registerStaff(e):
        addStaff(name.value, phone.value, email.value, rool.value, pw.value)

    btnRegStaff = ft.IconButton(icon=ft.icons.ADD_CIRCLE, on_click=registerStaff)

    content = ft.Column(
        [
            ft.Text("Register a new staff member", size=20),                
            name, 
            phone,
            email,
            rool,
            pw,
            btnRegStaff
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )       

            
    return content