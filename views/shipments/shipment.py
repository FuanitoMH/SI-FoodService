import flet as ft
from user_controls.app_nav import nav_view

def ShipmentView(page):
    # -- CONTROLS
    nav = nav_view(page)
    dwn_date = ft.Dropdown(label='Fecha', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("Todos"),
                                ft.dropdown.Option("Más reciente"),
                                ft.dropdown.Option("Más viejo"),
                            ])
    dwn_status = ft.Dropdown(label='Estatus', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("Todos"),
                                ft.dropdown.Option("entregado"),
                                ft.dropdown.Option("preparando"),
                                ft.dropdown.Option("en camino"),
                            ])
    btn_reset = ft.ElevatedButton(text='Reset', icon=ft.icons.RESTART_ALT, icon_color='#9AC8CD', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
    btn_NewShipment = ft.ElevatedButton( "Nuevo Envio", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)



    bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
    list_shipments = ft.Container(
                        content=ft.Column(
                            [   
                                ft.Row(
                                    [
                                        ft.Text(value='ID: 4', size=15, width=200, text_align=ft.TextAlign.START),
                                        ft.Row(
                                            [
                                                ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color="blue", icon_size=15,
                                                            tooltip='id'),
                                                ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED, icon_color="red", icon_size=15,
                                                            tooltip='id',)
                                            ], alignment=ft.MainAxisAlignment.END
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    spacing=0
                                ),
                                ft.Text(value='Fecha', size=15, width=200, text_align=ft.TextAlign.START),
                                ft.Container(content= ft.Text(value='en camino', size=15, color='#E9E8E8', text_align=ft.TextAlign.CENTER), 
                                                    border_radius=10, bgcolor='#6096B4', width=120),
                                ft.Text(value='No. Ordenes: 6', size=15),
                                ft.Text(value='Transportista: Medina Hernanadez', size=15),
                            ], 
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0
                        ),
                        width=300,
                        height=270,
                        padding=10,
                        bgcolor=bgColorCard, 
                        border_radius=ft.border_radius.all(5),
                )

    container_shipments = ft.Row(controls=[list_shipments, list_shipments, list_shipments, list_shipments, list_shipments, list_shipments, list_shipments, list_shipments, list_shipments],
                        wrap=True,
                        scroll='HIDDEN',
                        height=600,
                        width=1410,
                        run_spacing=20,
                        spacing=20
                    )

    content_main = ft.Column(
        [
            ft.Row(
                [   
                    dwn_date, 
                    dwn_status,
                    btn_reset,
                    btn_NewShipment
                ], 
                alignment=ft.MainAxisAlignment.START
            ),
            container_shipments
        ],
        alignment=ft.MainAxisAlignment.START,
        width=1450,
    ) 

    content = ft.Container(
        content=content_main
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