import flet as ft
from datetime import date, datetime
from user_controls.alert_dialog import AlertDialog

from models.shipment import get_shipment_by_id, post_shipment, set_status_shipment_ready
from models.staff import get_name_carriers
from models.cargo import post_cargo, get_orders_by_id_shipment, update_orders_status_onway_by_shiID
from models.order import get_orders_by_status_preparation, set_status_order_deliver

def ordenDetailsView(page, shipment_id:int=None):

    session_area = page.client_storage.get('session_area')

    def change_data(e):
        txt_shi_date.value = date_picker.value.date()
        txt_shi_date.update()

    # -- CONTROLS --
    txt_shi_id = ft.Text(value='ID: 4', size=15, width=200, text_align=ft.TextAlign.START)
    txt_shi_date = ft.Text(value=date.today(), size=16, weight=ft.FontWeight.BOLD)
    txt_shi_no_orders = ft.Text(size=16, width=600)
    txt_shi_carrier = ft.Text(size=16, width=600)
    txt_shi_status = ft.Text(value='en proceso', size=16, width=600)
    txt_none = ft.Text('')

    today = datetime.today()
    year = today.year
    month = today.month+1
    day = today.day
    if (month > 12):
        month = 1
        year += 1 
    last_date = datetime(year, month, day)

    date_picker = ft.DatePicker(
        on_change=change_data,
        on_dismiss=change_data,
        first_date=today,
        last_date=last_date,
    )

    page.overlay.append(date_picker)

    date_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_color='#e7f0f8',
        bgcolor='#6a7fc1',
        on_click=lambda _: date_picker.pick_date(),
    )

    # -- controls for select a carrier
    data_carriers = get_name_carriers()
    options_carriers = [ ft.dropdown.Option(f'{carrier.sta_id}: {carrier.sta_name} {carrier.sta_last_name}') for carrier in data_carriers]
    dwn_carrier = ft.Dropdown('Transportista', text_size=16, width=400, border='UNDERLINE',
                            options=options_carriers)
    btn_newShipment = ft.ElevatedButton("Crear Envío", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)

    # -- controls for select a order
    data_orders = get_orders_by_status_preparation()
    options_orders = [ ft.dropdown.Option(f'{order.ord_id}: {order.ord_cli_id.cli_name}') for order in data_orders]
    dwn_orders = ft.Dropdown('Ordenes', text_size=16, width=500, border='UNDERLINE', options=options_orders)


    # -- FUNCTIONS --
    def show_detail_shipment(id:int) -> None:
        global shipment_id
        shipment_id = id
        data = get_shipment_by_id(id)
        print(data)
        txt_shi_id.value = f"ID: {data.shi_id}"
        txt_shi_date.value = data.shi_date
        txt_shi_no_orders.value = f"No. Ordenes: {data.shi_no_orders}"
        txt_shi_carrier.value = f"{data.s.sta_name} {data.s.sta_last_name}"
        txt_shi_status.value = data.shi_status
        view.content = content_shipment_details
        if txt_shi_status.value != 'en proceso':
            cont_add_order.content = txt_none
            cntn_start_shipment.content = txt_none
        page.update()

    def create_shipment(e: ft.ControlEvent):
        id = post_shipment(txt_shi_date.value, no_orders=0, carrier_id=int(dwn_carrier.value.split(':')[0]))
        show_detail_shipment(id)

    def deliver_order(e: ft.ControlEvent):
        ord_id = e.control.tooltip
        set_status_order_deliver(ord_id)
        data_items = get_orders_by_id_shipment(shipment_id)
        items:list = draw_items(data_items)
        content_items.controls = items
        page.update()

    def begin_shipment(e: ft.ControlEvent):
        set_status_shipment_ready(shipment_id)
        txt_shi_status.value = 'listo'
        # set status order to 'en camino' 
        update_orders_status_onway_by_shiID(shipment_id)
        data_items = get_orders_by_id_shipment(shipment_id)
        items:list = draw_items(data_items)
        content_items.controls = items
        cntn_start_shipment.content = txt_none
        page.update()

    def draw_items(data):
        items = []
        for row in data:
            items.append(
                ft.Row(
                    [
                        ft.Text(value=row[0], size=16, width=270), # client name 
                        ft.Text(value=row[1], size=16, width=250), # client address
                        ft.Text(value=row[2], size=16, width=100), # order status
                        # row[3] is the order id
                        ft.ElevatedButton("Entregar Orden", tooltip=row[3], on_click=lambda e: deliver_order(e)) if session_area == 'transportista' and row[2] != 'entregado' else txt_none
                    ], alignment=ft.MainAxisAlignment.START
                )
            )
        return items
    
    def add_order_to_shipment(e: ft.ControlEvent):
        global shipment_id
        id_order = int(dwn_orders.value.split(':')[0])
        id_shipment = shipment_id
        post_cargo(id_order, id_shipment)

        # Update the list of orders
        data_items = get_orders_by_id_shipment(shipment_id)
        items = draw_items(data_items)
        content_items.controls = items

        show_detail_shipment(shipment_id)

        # update the dropdown of orders
        data_orders = get_orders_by_status_preparation()
        options_orders = [ ft.dropdown.Option(f'{order.ord_id}: {order.ord_cli_id.cli_name}') for order in data_orders]
        dwn_orders.options = options_orders
        page.update()

    # -- EVENTS --
    btn_newShipment.on_click = create_shipment
    
    # order container for shipping
    content_items = ft.Column()

    # -- CONTAINERS -- 
    if shipment_id != None:
        data_items = get_orders_by_id_shipment(shipment_id)
        items:list = draw_items(data_items)
        content_items.controls = items
        page.update()

    start_shipment = ft.ElevatedButton("Iniciar Envío", on_click=lambda e: begin_shipment(e))
    cntn_start_shipment = ft.Container(
        content=start_shipment
    )
    # Container to show orders from shipment
    content_orders = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Ordenes", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text("Nombre", size=16, weight=ft.FontWeight.BOLD, width=270, text_align=ft.TextAlign.START),
                        ft.Text("Dirección", size=16, weight=ft.FontWeight.BOLD, width=250),
                        ft.Text("Estado", size=16, weight=ft.FontWeight.BOLD, width=100),
                    ], alignment=ft.MainAxisAlignment.START
                ),
                content_items,
                cntn_start_shipment
            ]
        )
    )

    # Control to add a new order at shipment

    conten_add_new_order =ft.Row(
            [
                ft.Row([
                    dwn_orders,
                ], alignment=ft.MainAxisAlignment.START),
                ft.ElevatedButton("Agregar Orden", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN, on_click=lambda e: add_order_to_shipment(e)),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    
    cont_add_order = ft.Container(
        content=conten_add_new_order
    )

    # Container to show shipment details
    content_shipment_details = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Detalles Orden", size=20, weight=ft.FontWeight.BOLD),
                        txt_shi_id
                    ], width=600, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.DATE_RANGE_OUTLINED, color='#DD761C', size=12),
                        txt_shi_date,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.LOCAL_SHIPPING_ROUNDED, color='#DD761C', size=12),
                        txt_shi_carrier,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.INVENTORY_2_OUTLINED, color='#DD761C', size=12),
                        txt_shi_no_orders,  
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.INVENTORY_2_OUTLINED, color='#DD761C', size=12),
                        txt_shi_status,  
                    ]
                ),
                cont_add_order, 
                content_orders
            ]
        )
    )

    content_new_shipment = ft.Container(
        content=ft.Column(
            [
                ft.Text('Nuevo Envío', size=16, width=700, text_align='center'),
                ft.Row(
                    [
                        txt_shi_date, 
                        date_button
                    ], width=700, alignment=ft.MainAxisAlignment.CENTER),
                ft.Text('Seleccione a un Transportista:', size=16, width=700, text_align='start'),
                ft.Row([
                        dwn_carrier,
                        btn_newShipment
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=700
                )
            ], 
        )

    )


    view = ft.Container(
        content=content_new_shipment, 
        width=850,
        padding=15,
        bgcolor=ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100,
    )

    if shipment_id != None:
        show_detail_shipment(shipment_id)

    page.update()

    return view