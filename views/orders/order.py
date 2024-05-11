import flet as ft

from user_controls.app_nav import nav_view

def OrderView(page):
    # NAVIGATION
    nav = nav_view(page)


    content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("My Orders", size=30), 
                        ft.IconButton(icon=ft.icons.PRODUCTION_QUANTITY_LIMITS, icon_size=30),

                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            width=1450,

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