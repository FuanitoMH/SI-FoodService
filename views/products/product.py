import flet as ft

def ProductsView(page):
    
    content = ft.Column(
            [
                ft.Row(
                [
                    ft.TextField(
                        icon=ft.icons.SEARCH, 
                        width=850, 
                        label='Buscar',
                        border= 'none'
                    ),
                    ft.ElevatedButton(
                        "All", 
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE
                    ),
                    ft.Dropdown(
                        label='Categoria',
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE,
                        width=140,
                        border='none',
                        options=[
                            ft.dropdown.Option("All"),
                            ft.dropdown.Option("bebida"),
                            ft.dropdown.Option("comida"),
                            ft.dropdown.Option("acompañamiento"),
                            ]
                        ),
                    ft.Dropdown(
                        label='Temperatura',
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE,
                        width=140,
                        border='none',
                        options=[
                            ft.dropdown.Option("All"),
                            ft.dropdown.Option("seco"),
                            ft.dropdown.Option("refrigerado"),
                            ft.dropdown.Option("congelado"),
                            ]
                        ),
                    ft.ElevatedButton(
                        "Nuevo Producto", 
                        color=ft.colors.WHITE, 
                        width=120,
                        bgcolor=ft.colors.GREEN,
                        
                    )
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
                ft.Row(
                    [
                        ft.TextButton("Puros pinches productos", icon=ft.icons.WB_SUNNY_OUTLINED)
                    ],
                )
            ],
            width=1400
        )
    
    
    return content
