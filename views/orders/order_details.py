import flet as ft
from datetime import date
from user_controls.alert_dialog import AlertDialog

from models.client import get_name_clients, get_one_client_by_id
from models.order import post_order, get_order_join_client_by_id
from models.orderitems import post_item, get_items_by_id_order
from models.product import get_name_products


def ordenDetailsView(page, order_id:int=None):
    ord_id = order_id

    data_clients = get_name_clients()
    options_clients = [ ft.dropdown.Option(f'{client.cli_id}: {client.cli_name}') for client in data_clients]

    # Controls 
    alert_dialog = AlertDialog(page)
    txt_ord_id = ft.Text(value=order_id)
    dwn_client = ft.Dropdown('Cliente', text_size=16, width=650, border='UNDERLINE',
                            options=options_clients)
    txt_date = ft.Text(value=date.today(), size=16)

    txt_cli_name = ft.Text(size=16, width=600)
    txt_cli_id = ft.Text("ID: ", size=16, width=600)
    txt_cli_address = ft.Text("Direccion: ", size=16, width=600)
    txt_cli_phone = ft.Text("Telefono: ", size=16, width=600)
    txt_status = ft.Text(value="en proceso", size=16, width=600)
    btn_create_ord = ft.ElevatedButton("Crear Orden", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)

    # -- FUNCTIONS --
    def format_phone(number: str) -> str:
        return f'({number[:3]}) {number[3:6]}-{number[6:]}'

    #############
    def create_order(e: ft.ControlEvent):
        id = post_order(int(txt_cli_id.value.split(":")[1]), txt_date.value, txt_status.value)
        txt_ord_id.value = id
        content.content = content_order
        page.update()

    def show_client(e: ft.ControlEvent):
        data = get_one_client_by_id(dwn_client.value.split(":")[0])
        txt_cli_id.value = f"ID: {data.cli_id}"
        txt_cli_name.value = data.cli_name
        txt_cli_address.value = data.cli_address
        txt_cli_phone.value = format_phone(data.cli_phone)
        content_info_client.content = ft.Column(
            [
                txt_cli_id,
                ft.Row([
                    ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color='#DD761C', size=12),
                    txt_cli_address,  
                ]),
                ft.Row([
                    ft.Icon(name=ft.icons.PHONE_OUTLINED, color='#DD761C', size=12),
                    txt_cli_phone,  
                ]),
                ft.Row([
                    btn_create_ord
                ], alignment=ft.MainAxisAlignment.CENTER, width=600,
                )
            ]
        )
        page.update()

    def show_details_order(id:int=None): 
        data = get_order_join_client_by_id(id)
        txt_cli_id.value = f"ID: {data[0].c.cli_id}"
        txt_cli_name.value = data[0].c.cli_name
        txt_cli_address.value = data[0].c.cli_address
        txt_cli_phone.value = format_phone(data[0].c.cli_phone)
        content.content = content_order
        page.update()

    def draw_items(data):
        items = []
        for item in data:
            items.append(
                ft.Row(
                    [
                        ft.Text(item.p.pro_name, size=16, width=300, text_align=ft.TextAlign.START),
                        ft.Text(item.itm_stock, size=16, width=200),
                    ], alignment=ft.MainAxisAlignment.START
                )
            )
        return items
    
    def add_product_to_order(e: ft.ControlEvent):
        ord_id = txt_ord_id.value
        post_item(ord_id, int(dwn_products.value.split(":")[0]), txt_stock.value)
        data = get_items_by_id_order(ord_id)
        items:list = draw_items(data)
        content_items.controls = items
        page.update()


    # -- EVENTS --
    dwn_client.on_change = show_client
    btn_create_ord.on_click = create_order

    data_products = get_name_products()
    options_products = [ft.dropdown.Option(f'{product.pro_id}: {product.pro_name}') for product in data_products]
    dwn_products = ft.Dropdown('Productos', text_size=16, width=250, border='UNDERLINE', options=options_products)
    txt_stock = ft.TextField(label='Cantidad', text_size=16, width=100, border='none')

    # -- CONTAINERS --
    data = get_items_by_id_order(ord_id)
    items:list = draw_items(data)

    content_items = ft.Column(controls=items)
    content_products = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Productos", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text("Nombre", size=16, weight=ft.FontWeight.BOLD, width=300, text_align=ft.TextAlign.START),
                        ft.Text("Cantidad", size=16, weight=ft.FontWeight.BOLD, width=200),
                    ], alignment=ft.MainAxisAlignment.START
                ),
                content_items
            ]
        )
    )

    # Container to show order details
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
                        txt_cli_address,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.PHONE_OUTLINED, color='#DD761C', size=12),
                        txt_cli_phone,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Row([
                            dwn_products,
                            txt_stock,
                        ], alignment=ft.MainAxisAlignment.START),
                        ft.ElevatedButton("Agregar Producto", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN, on_click=lambda e: add_product_to_order(e)),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                content_products
            ]
        )
    )

    # Container to show controls to create new order
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
    
    if ord_id != None:
        show_details_order(ord_id)

    page.update()

            
    return content