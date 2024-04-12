import flet as ft
from models.staff import logginStaff


def logginView(page: ft.Page):

    def closeAlert(e):
        alet_error.open = False
        page.update()

    def showAlert():
        page.dialog = alet_error
        alet_error.open = True
        text_email.value = ""
        text_passw.value = ""
        page.update()
    

    text_email: ft.TextField     = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=200)
    text_passw: ft.TextField     = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=200, password=True)
    btn_login: ft.ElevatedButton = ft.ElevatedButton("Aceptar", width=200, disabled=True)
    btn_register: ft.CupertinoButton  = ft.CupertinoButton(
                content=ft.Text("Registrarse", size=12),
                width=200, color=ft.colors.BLUE_200)
    
    alet_error: ft.AlertDialog   = ft.AlertDialog(
                title=ft.Text("Usuario no encontrado", size=22, color=ft.colors.RED, text_align=ft.TextAlign.CENTER),
                content=ft.Text("El correo o la contraseña son incorrectos", size=12),
                actions=[
                    ft.TextButton("Aceptar", on_click=closeAlert)
                ],actions_alignment=ft.MainAxisAlignment.END
                )
   
    def loggin(e):
        query = logginStaff(text_email.value, text_passw.value)
        
        if query.count() == 0:
            print('Usuario no encontrado')
            btn_login.disabled = True
            showAlert()
        else:
            sessionId = None 
            for staff in query:
                sessionId = staff.sta_id
                sessionName = staff.sta_name

            page.client_storage.set("session", sessionId)
            print(f'loggin {sessionName}')

            page.go('/')
            
    def register(e):
        page.go('/staff')

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
                    btn_login,
                    btn_register,
                    alet_error
                ]
            ) 
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    return content
        

if __name__ == '__main__':
    logginView()
