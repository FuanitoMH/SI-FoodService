import flet as ft
from datetime import date
from user_controls.alert_dialog import AlertDialog

from models.client import get_name_clients, get_one_client_by_id
from models.order import post_order


def ordenDetailsView(page, id:int=None):

    data_clients = get_name_clients()
    options_clients = [ ft.dropdown.Option(f'{client.cli_id}: {client.cli_name}') for client in data_clients]

    # Controls 
    alert_dialog = AlertDialog(page)
    
    dwn_client = ft.Dropdown('Cliente', text_size=16, width=650, border='UNDERLINE',
                            options=options_clients)
    txt_cli_name = ft.Text(size=16, width=600)
    txt_date = ft.Text(value=date.today(), size=16)

    txt_cli_id = ft.Text("ID: ", size=16, width=600)
    txt_address = ft.Text("Direccion: ", size=16, width=600)
    txt_phone = ft.Text("Telefono: ", size=16, width=600)
    txt_status = ft.Text("en preparacion", size=16, width=600)
    btn_create_ord = ft.ElevatedButton("Crear Orden", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)

    # -- FUNCTIONS --
    def format_phone(number: str) -> str:
        return f'({number[:3]}) {number[3:6]}-{number[6:]}'

    def create_order(e: ft.ControlEvent):
        post_order(int(txt_cli_id.value.split(":")[1]), txt_date.value, txt_status.value)
        content.content = content_order
        page.update()

    def show_client(e: ft.ControlEvent):
        data = get_one_client_by_id(dwn_client.value.split(":")[0])
        txt_cli_id.value = f"ID: {data.cli_id}"
        txt_cli_name.value = data.cli_name
        txt_address.value = data.cli_address
        txt_phone.value = format_phone(data.cli_phone)
        content_info_client.content = ft.Column(
            [
                txt_cli_id,
                ft.Row([
                    ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color='#DD761C', size=12),
                    txt_address,  
                ]),
                ft.Row([
                    ft.Icon(name=ft.icons.PHONE_OUTLINED, color='#DD761C', size=12),
                    txt_phone,  
                ]),
                ft.Row([
                    btn_create_ord
                ], alignment=ft.MainAxisAlignment.CENTER, width=600,
                )
            ]
        )
        page.update()


    # -- EVENTS --
    dwn_client.on_change = show_client
    btn_create_ord.on_click = create_order

    # -- CONTAINERS --
    content_products = ft.Container(
        content=ft.Text("Productos", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, width=600)
    )
    content_order = ft.Container(
        content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Detalles Orden", size=20, weight=ft.FontWeight.BOLD),
                        txt_date
                    ], width=600, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                txt_cli_name,
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color='#DD761C', size=12),
                        txt_address,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.PHONE_OUTLINED, color='#DD761C', size=12),
                        txt_phone,  
                    ]
                ),
                content_products
            ]
        )
    )

    content_info_client = ft.Container()
    content_new_order = ft.Container(
        content=ft.Column(
            [
                    ft.Text("Nueva Orden", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, width=600),    
                    ft.Text("Seleccione un cliente", size=16),    
                    dwn_client,
                    ft.Row([
                        ft.Text("Fecha: ", size=16, weight=ft.FontWeight.BOLD),
                        txt_date
                    ]),
                    content_info_client
            ],
        )        
    )  

    content = ft.Container(
        content=content_new_order, 
        width=600,
        padding=15,
        bgcolor=ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100,
    )
    
         

    page.update()

            
    return content