import flet as ft

def ShipmentView(page):

    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text("My shipments", size=30), 
                    ft.IconButton(icon=ft.icons.PRODUCTION_QUANTITY_LIMITS, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    return content