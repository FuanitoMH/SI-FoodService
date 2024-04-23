import flet as ft
from views.FletRouter import Router

from user_controls.app_bar import NavBar
 
 
def main(page: ft.Page):
    page.theme_mode = 'dark'

    page.appbar = NavBar(page)
    myRouter = Router(page)
    
    page.on_route_change = myRouter.route_change
    page.add(
        myRouter.body
    )

    if page.client_storage.get('session') == None:
        page.go("/home")
    else:
        page.go("/home")

ft.app(target=main, assets_dir="assets")