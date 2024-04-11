import flet as ft


def IndexView(page):

    # Controls
    text = ft.Text("Welcome", size=50)
    
    session = page.client_storage.get('session')
    if session != None:
        text.value = f"Welcome {session}"
    print(session, '/index')

    content = ft.Column(
        [  
            ft.Row(
                [
                    text
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )
    

    return content


if __name__ == '__main__':
    IndexView()