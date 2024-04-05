import flet as ft
from models.staff import logginStaff
# from login import Login

def logginView(page):
    
    session = page.client_storage.get('session')
    if session == None:
        print('Aun NO logeado /loggin')
        

    email = ft.TextField(label="Correo", text_align=ft.TextAlign.LEFT, width=200)
    pw = ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT, width=200)
    
   
    def loggin(e):
        query = logginStaff(email.value, pw.value)
        
        if query.count() == 0:
            print('Usuario no encontrado')
        else:
            sessionId = None 
            for staff in query:
                sessionId = staff.sta_id

            e.page.client_storage.set("session", sessionId)
            print(e.page.client_storage.get('session'), 'session /loggin')
            
            page.go('/')
            

    btnLoggin = ft.IconButton(icon=ft.icons.ADD_CIRCLE, on_click=loggin)

    content = ft.Column(
        [
            ft.Text("Loggin", size=20),       
            email,
            pw,
            btnLoggin
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )       

            
    return content

if __name__ == '__main__':
    logginView()
