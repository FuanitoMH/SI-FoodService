import flet as ft
from models.staff import logginStaff
from user_controls.alert_dialog import AlertDialog


def logginView(page: ft.Page):

    text_email: ft.TextField     = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=300, border='underline')
    text_passw: ft.TextField     = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=300, password=True, border='underline')
    btn_login: ft.ElevatedButton = ft.ElevatedButton("Aceptar", width=200, disabled=True)
    btn_register: ft.CupertinoButton  = ft.CupertinoButton(
                content=ft.Text("Registrarse", size=12),
                width=200, color=ft.colors.BLUE_200)
    
    alert_dialog = AlertDialog(page)
   
    def loggin(e):
        query = logginStaff(text_email.value, text_passw.value)
        
        if query.count() == 0:
            print('Usuario no encontrado')
            btn_login.disabled = True
            alert_dialog.show(title="ERROR", content="Correo o Contraseña incorrectos", status="error")
        else:
            sessionId = None 
            session_area = None
            for staff in query:
                sessionId = staff.sta_id
                sessionName = staff.sta_name
                session_area = staff.sta_area

            page.client_storage.set("session", sessionId)
            page.client_storage.set("session_area", session_area)
            print(f'loggin {sessionName}')

            page.go('/home')
            
    def register(e):
        page.go('/staff/register')

    def validateInput(e: ft.ControlEvent) -> None:
        if all([text_email.value, text_passw.value]):
            btn_login.disabled = False
        else:
            btn_login.disabled = True
        page.update()

    text_email.on_change = validateInput
    text_passw.on_change = validateInput
    btn_login.on_click = loggin
    btn_register.on_click = register

    content = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Iniciar Sesión", size=20),       
                    text_email,
                    text_passw,
                    ft.Row([btn_login], width=300, alignment=ft.MainAxisAlignment.CENTER),
                    # btn_register
                ], alignment=ft.MainAxisAlignment.CENTER, height=400
            ) 
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    return content
        

if __name__ == '__main__':
    logginView()
