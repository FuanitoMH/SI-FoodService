import flet as ft
from user_controls.app_nav import nav_view
from views.orders.order_details import ordenDetailsView
from models.order import get_order_join_client, get_order_by_date, get_orders_by_status



def OrdersView(page):
    # -- CONTROLS
    nav = nav_view(page)
    dwn_date = ft.Dropdown(label='Fecha', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("Todos"),
                                ft.dropdown.Option("Más reciente"),
                                ft.dropdown.Option("Más antigua"),
                            ])
    dwn_status = ft.Dropdown(label='Estado', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option('Todos'),
                                ft.dropdown.Option('en proceso'),
                                ft.dropdown.Option('listo'),
                                ft.dropdown.Option('en camino'),
                                ft.dropdown.Option('entregado'),
                            ])
    btn_reset = ft.ElevatedButton(text='Reset', icon=ft.icons.RESTART_ALT, icon_color='#9AC8CD')
    btn_NewOrder = ft.ElevatedButton( "Nueva Orden", color=ft.colors.WHITE, width=140, bgcolor=ft.colors.GREEN)
    btn_cancel = ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.RED)


    # -- FUNCTIONS --
    def format_phone(number: str) -> str:
        return f'({number[:3]}) {number[3:6]}-{number[6:]}'
    
    def cancelRegister(e):
        list_orders = []
        data_orders = get_order_join_client()
        list_orders = draw_order(data_orders)
        container_orders.controls = list_orders
        content.content = content_main
        page.update()

    def newOrder(e):
        view_order.content = ordenDetailsView(page)
        content.content = content_order
        page.update()

    def view_details(e:ft.ControlEvent):
        id = e.control.tooltip
        view_order.content = ordenDetailsView(page, id)
        content.content = content_order
        page.update()

    bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
    def draw_order(data):
        list_orders = []
        for d in data:
            list_orders.append(
                ft.Container(
                    content=ft.Column(
                        [   
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(value=f'ID: {d.ord_id}', size=15, width=200, text_align=ft.TextAlign.START),
                                            ft.Row(
                                                [
                                                    ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color="blue", icon_size=15,
                                                                tooltip=d.ord_id, on_click=lambda e: view_details(e)),
                                                    ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED, icon_color="red", icon_size=15,
                                                                tooltip='id',)
                                                ], alignment=ft.MainAxisAlignment.END
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        spacing=0
                                    ),
                                    ft.Text(value=f'{d.c.cli_name}', size=15, weight=ft.FontWeight.BOLD, width=300, text_align=ft.TextAlign.CENTER),
                                    ft.Row(
                                        [
                                            ft.Text(value=d.ord_date, size=15, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START),
                                            ft.Container(content= ft.Text(value=d.ord_status, size=15, color='#2c3d4d', text_align=ft.TextAlign.CENTER), 
                                                    border_radius=10, bgcolor='#91b9cf', width=120)
                                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color='#DD761C', size=12),
                                            ft.Text(value=f'{d.c.cli_address}'[0:35], size=15), 
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(name=ft.icons.PHONE_OUTLINED, color='#DD761C', size=12),
                                            ft.Text(value=format_phone(d.c.cli_phone), size=15)
                                        ]
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10
                            ),
                            ft.ElevatedButton( "Ver Detalles", width=130, bgcolor=ft.colors.BLUE_300, color=ft.colors.WHITE, tooltip=d.ord_id, on_click=lambda e: view_details(e) )
                        ], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0
                    ),
                    width=300,
                    height=250,
                    padding=10,
                    bgcolor=bgColorCard, 
                    border_radius=ft.border_radius.all(5),
                )
            )
        return list_orders

    def order_by_date(e):
        data_orders = (get_order_by_date(dwn_date.value) if dwn_date.value != 'Todos' else get_order_join_client())
        list_orders = draw_order(data_orders)
        container_orders.controls = list_orders
        dwn_status.value = ''
        page.update()

    def order_by_status(e):
        data_orders = (get_orders_by_status(dwn_status.value) if dwn_status.value != 'Todos' else get_order_join_client())
        list_orders = draw_order(data_orders)
        container_orders.controls = list_orders
        dwn_date.value = ''
        page.update()

    def reset(e:ft.ControlEvent):
        dwn_date.value = ''
        dwn_status.value = ''
        data_orders = get_order_join_client()
        list_orders = draw_order(data_orders)
        container_orders.controls = list_orders
        page.update()

    # -- EVENTS --
    btn_cancel.on_click = cancelRegister
    btn_NewOrder.on_click = newOrder
    dwn_date.on_change = order_by_date
    dwn_status.on_change = order_by_status
    btn_reset.on_click = reset

    # -- VARIABLES --
    data_orders = get_order_join_client()
    list_orders = draw_order(data_orders)


    container_orders = ft.Row(controls=list_orders,
                        wrap=True,
                        scroll='HIDDEN',
                        height=650,
                        width=1410,
                        run_spacing=20,
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
    

    view_order = ft.Container(
        content=ordenDetailsView(page)
    )

    # -- CONTAINERS --
    content_order = ft.Column(
        [
            ft.Row(
                [
                    btn_cancel,
                ],
                width=600,
                alignment=ft.MainAxisAlignment.END
            ),
            view_order
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=1450,
    )

    content_main = ft.Column(
        [
            ft.Row(
                [   
                    dwn_date,
                    dwn_status,
                    btn_reset,
                    btn_NewOrder
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            container_orders
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