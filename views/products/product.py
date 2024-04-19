import flet as ft

def ProductsView(page):
    
    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text("My Products", size=30), 
                    ft.IconButton(icon=ft.icons.PRODUCTION_QUANTITY_LIMITS, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.TextButton("Puros pinches productos", icon=ft.icons.WB_SUNNY_OUTLINED)
                    ],
                ),
                ft.Row(
                    [
                        ft.TextButton("Holaaa", icon=ft.icons.CLOSE, icon_color="red")
                    ]
                ),
            ]
        )
    
    
    return content
