import flet as ft

def IndexView(page):

    session = page.client_storage.get('session')
    print(session, '/index')
    
    if session == None:
        print('NO LOGGEADO /index')
        page.go('/loggin')
            

    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text(
                        "Welcome to my Flet Router Tutorial " + str(session),
                        size=50)
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            )
            ]
    
    )
    
    return content

if __name__ == '__main__':
    IndexView()