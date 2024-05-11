import flet as ft

from user_controls.app_nav import nav_view


def HomeView(page):

    image_src = "../assets/logo-FSG.png" if page.theme_mode == "dark" else "../assets/logo-FSG-blue.png"
    
    nav = nav_view(page)

    content = ft.Column(
            [
                ft.Text("Bienvenido a Sistema de información de FoodService", size=25),
                ft.Image(
                    src=image_src,
                    width=400,
                    height=360,
                ),
            ],
            width=1400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    view = ft.Container(
        content=ft.Row(
            controls=[
                nav, 
                content
            ], 
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )
    
    return view


if __name__ == '__main__':
    HomeView()