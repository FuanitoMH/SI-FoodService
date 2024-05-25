import flet as ft 
from user_controls.app_nav import nav_view
from user_controls.alert_dialog import AlertDialog
from models.client import get_clients, get_client_by_name, delete_client_by_id


def ClientView(page: ft.Page):

    # -- CONTROLS --
    nav = nav_view(page)
    alert_dialog = AlertDialog(page)
    text_search = ft.TextField(icon=ft.icons.SEARCH, width=600, label='Buscar', border= 'UNDERLINE', border_color=ft.colors.WHITE)
    btn_NewClient = ft.ElevatedButton( "Nuevo Cliente", color=ft.colors.WHITE, width=140, bgcolor=ft.colors.GREEN, 
                                      icon=ft.icons.PERSON_ADD_OUTLINED, icon_color=ft.colors.WHITE)
    

    # -- FUNCTIONS --
    def delete_client(e: ft.ControlEvent):
        delete_client_by_id(e.control.tooltip)
        data_clients = get_clients()
        list_clients = []
        list_clients = draw_clients(data_clients)
        container_clients.controls = list_clients
        page.update()
        alert_dialog.show('Cliente eliminado', 'El cliente ha sido eliminado correctamente', status='info')


    def show_phone(number: str) -> str:
        return f'({number[:3]}) {number[3:6]}-{number[6:]}'


    def draw_clients(data_clients):
        clients = []
        text_size = 15
        for client in data_clients:
            clients.append(
                ft.Container( 
                    bgcolor=ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100, 
                    padding=10, width=1400,
                    content=ft.Row(
                        [   
                            ft.Icon(name=ft.icons.PERSON_OUTLINED, color=ft.colors.PINK),
                            ft.Column(
                                [
                                    ft.Text(value=client.cli_name, size=text_size+2),
                                    ft.Row(
                                        [
                                            ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color='#DD761C', size=12),
                                            ft.Text(value=client.cli_address[0:60], size=text_size-4),
                                        ], spacing=5
                                    )
                                ],width=350, alignment=ft.MainAxisAlignment.START
                            ),
                            ft.Text(value=client.cli_email, size=text_size, text_align=ft.TextAlign.CENTER, width=250),
                            ft.Text(value=show_phone(client.cli_phone), size=text_size, text_align=ft.TextAlign.CENTER, width=225),
                            ft.Text('403', size=text_size, text_align=ft.TextAlign.CENTER, width=225),
                            ft.Row(
                                [
                                    ft.IconButton( icon=ft.icons.DELETE_FOREVER_OUTLINED, icon_color="red400", icon_size=25, tooltip=client.cli_id, on_click=delete_client),
                                    ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color="blue400", icon_size=25, tooltip=client.cli_id, )
                                ],width=150, alignment=ft.MainAxisAlignment.END
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    )
                )
            )
        return clients


    def search_by_name(e: ft.ControlEvent):
        data_clients = get_client_by_name(text_search.value)
        list_clients = []
        list_clients = draw_clients(data_clients)
        container_clients.controls = list_clients
        page.update()
    

    # -- VARIABLES --
    list_clients = []
    data_clients = get_clients()
    list_clients = draw_clients(data_clients)
    text_search.on_change = search_by_name


    # -- EVENTS --
    btn_NewClient.on_click = lambda e: page.go('/clients/register')


    # -- CONTENT --
    text_size = 15
    row_header_client = ft.Container(width=1400,
        content=ft.Row(
            [   
                ft.Text('Información Cliente', size=text_size, width=380, text_align=ft.TextAlign.START),
                ft.Text('Correo', size=text_size, width=270, text_align=ft.TextAlign.CENTER),
                ft.Text('Teléfono', size=text_size, width=215, text_align=ft.TextAlign.CENTER),
                ft.Text('No. Pedidos', size=text_size, width=230, text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )
    

    container_clients=ft.Column(
            controls=list_clients,
            alignment=ft.MainAxisAlignment.START,
            scroll='ALWAYS',
            width=1415,
            height=600
        )


    content = ft.Column(
        [
            ft.Row(
                [   
                    text_search,
                    btn_NewClient
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=1300
            ),
            row_header_client,
            container_clients
        ],
        alignment=ft.MainAxisAlignment.START,
        width=1420,

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
