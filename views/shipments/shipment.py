import flet as ft
from user_controls.app_nav import nav_view
from views.shipments.shipment_details import ordenDetailsView

from models.shipment import get_shipments, delete_shipment, get_shipments_by_date


def ShipmentView(page):
    # -- CONTROLS
    nav = nav_view(page)
    dwn_date = ft.Dropdown(label='Fecha', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("Todos"),
                                ft.dropdown.Option("Más reciente"),
                                ft.dropdown.Option("Más antigua"),
                            ])
    btn_reset = ft.ElevatedButton(text='Reset', icon=ft.icons.RESTART_ALT, icon_color='#9AC8CD')
    btn_NewShipment = ft.ElevatedButton( "Nuevo Envio", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)
    btn_cancel = ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.RED)

    # -- FUNCTIONS --
    def new_shipment(e: ft.ControlEvent):
        view_shipment.content = ordenDetailsView(page)
        content.content = content_shipment_details
        page.update()

    def show_details(e:ft.ControlEvent):
        id = e.control.tooltip
        view_shipment.content = ordenDetailsView(page, id)
        content.content = content_shipment_details
        page.update()
    
    def delete(e: ft.ControlEvent):
        id = e.control.tooltip
        delete_shipment(id)
        data_shipments = get_shipments()
        list_shipments = draw_shipments(data_shipments)
        container_shipments.controls = list_shipments
        content.content = content_main
        page.update()

    def search_by_date(e: ft.ControlEvent):
        data_shipments = get_shipments_by_date(dwn_date.value) if dwn_date.value != 'Todos' else get_shipments()
        list_shipments = draw_shipments(data_shipments)
        container_shipments.controls = list_shipments
        content.content = content_main
        page.update()

    def reset(e: ft.ControlEvent):
        data_shipments = get_shipments()
        list_shipments = draw_shipments(data_shipments)
        container_shipments.controls = list_shipments
        content.content = content_main
        dwn_date.value = ''
        page.update()
    
    def cancelRegister(e):
        data_shipments = get_shipments()
        list_shipments = draw_shipments(data_shipments)
        container_shipments.controls = list_shipments
        content.content = content_main
        page.update()


    bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
    def draw_shipments(data):
        shipments_list = []
        for item in data:
            shipments_list.append(
                ft.Container(
                    content=ft.Column(
                        [   
                             ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(value=f'ID: {item.shi_id}', size=15, width=200, text_align=ft.TextAlign.START),
                                            ft.Row(
                                                [
                                                    ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color="blue", icon_size=15,
                                                                tooltip=item.shi_id, on_click=lambda e: show_details(e)),
                                                    ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED, icon_color="red", icon_size=15,
                                                                tooltip=item.shi_id, on_click=lambda e: delete(e))
                                                ], alignment=ft.MainAxisAlignment.END
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        spacing=0
                                    ),
                                    ft.Text(value=item.shi_date, size=15, width=300, text_align=ft.TextAlign.CENTER, weight='BOLD'),
                                    ft.Text(value=f'No. Ordenes: {item.shi_no_orders}', size=15),
                                    ft.Text(value=f'Transportista: {item.s.sta_name} {item.s.sta_last_name}', size=15),
                                ]
                            ),
                            
                            ft.ElevatedButton( "Ver Detalles", width=130, bgcolor=ft.colors.BLUE_300, color=ft.colors.WHITE, tooltip=item.shi_id, on_click=lambda e: show_details(e) )
                        ], 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=0
                    ),
                    width=300,
                    height=250,
                    padding=10,
                    bgcolor=bgColorCard, 
                    border_radius=ft.border_radius.all(5),
                )
            ) 
        return shipments_list
    

    # -- EVENTS --
    btn_cancel.on_click = cancelRegister
    btn_NewShipment.on_click = new_shipment
    dwn_date.on_change = search_by_date
    btn_reset.on_click = reset


    view_shipment = ft.Container(
        # content=ordenDetailsView(page)
    )

    # -- CONTAINER --
    content_shipment_details = ft.Column(
        [
            ft.Row(
                [
                    btn_cancel,
                ],
                width=750,
                alignment=ft.MainAxisAlignment.END
            ),
            view_shipment
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=1450,
    )

    data_shipments = get_shipments()
    list_shipments = draw_shipments(data_shipments)

    container_shipments = ft.Row(controls=list_shipments,
                        wrap=True,
                        scroll='HIDDEN',
                        height=600,
                        width=1410,
                        run_spacing=20,
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    )

    content_main = ft.Column(
        [
            ft.Row(
                [   
                    dwn_date, 
                    btn_reset,
                    btn_NewShipment
                ], 
                alignment=ft.MainAxisAlignment.CENTER
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

    page.update()

    return view