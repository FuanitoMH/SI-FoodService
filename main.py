import flet as ft
import asyncio
from views.FletRouter import Router


from user_controls.app_bar import NavBar
from views.loggin_view import logginView
 
 
def main(page: ft.Page):
    page.theme_mode = "dark"

    page.appbar = NavBar(page)
    myRouter = Router(page)
    
    page.on_route_change = myRouter.route_change
    page.add(
        myRouter.body
    )

    if page.client_storage.get('session') == None:
        page.go("/login")
    else:
        page.go("/")

ft.app(target=main, assets_dir="assets")