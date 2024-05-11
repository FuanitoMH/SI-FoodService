import flet as ft
from views.FletRouter import Router

from user_controls.app_bar import NavBar
 
 
def main(page: ft.Page):
    page.theme_mode = 'dark'
    # page.window_width = 1500
    # page.window_height = 900
    # page.window_full_screen = True
    page.window_top = 0
    page.window_resizable = True  # window is not resizable

    page.appbar = NavBar(page)
    myRouter = Router(page)
    
    page.on_route_change = myRouter.route_change
    page.add(
        myRouter.body
    )

    if page.client_storage.get('session') == None:
        page.go("/login")
    else:
        page.go("/home")

ft.app(target=main, assets_dir="assets")