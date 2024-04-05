import flet as ft
from views.FletRouter import Router
from user_controls.app_bar import NavBar

# from login import Login 
 
 
def main(page: ft.Page):
    page.theme_mode = "dark"

    print(page.client_storage.get('session'), '/main')
    if page.client_storage.get('session') == None:
        print('No Loggeado /main')
        page.go('/loggin')

    page.appbar = NavBar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    
    page.add(
        myRouter.body
    )

    page.update()

ft.app(target=main, assets_dir="assets")