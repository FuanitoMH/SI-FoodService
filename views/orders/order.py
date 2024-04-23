import flet as ft

def OrderView(page):

    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text("My Orders", size=30), 
                    ft.IconButton(icon=ft.icons.PRODUCTION_QUANTITY_LIMITS, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    return content