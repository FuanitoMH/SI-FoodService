import flet as ft
from user_controls.alert_dialog import AlertDialog
from user_controls.app_nav import nav_view
from views.staff.staff_register import registerStaffView
from models.staff import get_staff, get_staff_by_name, get_staff_by_area, delete_staff_by_id


def StaffView(page):
    options_area = [
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Compras"),
            ft.dropdown.Option("ventas"),
            ft.dropdown.Option("envios"),
            ft.dropdown.Option("transportista"),
            ft.dropdown.Option("recursos humanos"),
        ]
    if page.client_storage.get('session_area') == 'admin':
        options_area.append( ft.dropdown.Option("admin") )


    nav = nav_view(page)
    alert_dialog = AlertDialog(page)

    text_search = ft.TextField(icon=ft.icons.SEARCH, width=500, label='Buscar', border= 'UNDERLINE', border_color=ft.colors.WHITE)
    btn_NewStaff = ft.ElevatedButton( "Nuevo Trabajador", color=ft.colors.WHITE, width=130, bgcolor=ft.colors.GREEN)
    dwn_area = ft.Dropdown(label='Área', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=options_area)
    btn_reset = ft.ElevatedButton(text='Reset', icon=ft.icons.RESTART_ALT, icon_color='#9AC8CD')
    btn_cancel = ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.RED)

    view_register = ft.Container(
        content=registerStaffView(page)
    )
    
    

    # -- FUNCTIONS --
    def registerStaff(e):
        view_register.content = registerStaffView(page)
        content.content = content_register
        content.update()

    def update_staff(e):
        view_register.content = registerStaffView(page, int(e.control.tooltip))
        content.content = content_register
        content.update()

    def cancelRegister(e):
        list_staff = []
        data_staff = get_staff()
        list_staff = draw_staff(data_staff)
        staff.controls = list_staff
        content.content = content_staff
        page.update()

    def search_by_name(e):
        list_staff = []
        data_staff = get_staff_by_name(text_search.value)
        list_staff = draw_staff(data_staff)
        staff.controls = list_staff
        dwn_area.value = ''
        page.update()

    def search_by_area(e):
        list_staff = []
        data_staff = get_staff_by_area(dwn_area.value) if dwn_area.value != 'Todos' else get_staff()
        list_staff = draw_staff(data_staff)
        staff.controls = list_staff
        text_search.value = ''
        page.update()

    def reset_search(e):
        data_staff = get_staff()
        list_staff = draw_staff(data_staff)
        staff.controls = list_staff
        text_search.value = ''
        dwn_area.value = ''
        page.update()

    def delete_staff(e: ft.ControlEvent):
        print(e.control.tooltip)
        delete_staff_by_id(e.control.tooltip)
        data_staff = get_staff()
        list_staff = draw_staff(data_staff)
        staff.controls = list_staff
        page.update()
        alert_dialog.show('Trabajador eliminado', 'El trabajador ha sido eliminado correctamente', status='info')

    def show_phone(number: str) -> str:
        return f'({number[:3]}) {number[3:6]}-{number[6:]}'


    def draw_staff(data_staff):
        staffs = []
        bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
        
        for staff in data_staff:
            staffs.append(
                ft.Container(
                        content=ft.Column(
                            [   
                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.icons.EDIT_OUTLINED, icon_color="blue", icon_size=15,
                                                    tooltip=staff.sta_id, on_click=lambda e: update_staff(e)),
                                        ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED, icon_color="red", icon_size=15,
                                                    tooltip=staff.sta_id, on_click=lambda e: delete_staff(e))
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=0
                                ),
                                ft.Text(value=f'{staff.sta_name} {staff.sta_last_name}'.upper(), size=15, width=200, text_align=ft.TextAlign.CENTER),
                                ft.Icon(name=ft.icons.FACE_OUTLINED, size=60),
                                ft.Text(value=staff.sta_email, size=15),
                                ft.Text(value=show_phone(staff.sta_phone), size=15),
                                ft.Container(content= ft.Text(value=staff.sta_area, size=15, color='#E9E8E8', text_align=ft.TextAlign.CENTER), 
                                                    border_radius=10, bgcolor='#6096B4', width=120)
                            ], 
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0
                        ),
                        width=270,
                        height=270,
                        padding=10,
                        bgcolor=bgColorCard, 
                        border_radius=ft.border_radius.all(5),
                )
            )
        return staffs

    # -- VARIABLES --
    list_staff = []
    data_staff = get_staff()
    list_staff = draw_staff(data_staff)

    staff = ft.Row(controls=list_staff,
                        wrap=True,
                        scroll='HIDDEN',
                        height=600,
                        width=1410,
                        run_spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
    
    
    # -- EVENTS --
    btn_NewStaff.on_click = registerStaff
    btn_cancel.on_click = cancelRegister
    text_search.on_change = search_by_name
    dwn_area.on_change = search_by_area
    btn_reset.on_click = reset_search


    # -- CONTAINERS --
    
    content_register = ft.Column(
        [
            ft.Row(
                [
                    btn_cancel,
                ],
                width=500,
                alignment=ft.MainAxisAlignment.END
            ),
            view_register
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=1450,
    )

    content_staff = ft.Column(
        [
            ft.Row(
                [   
                    text_search,
                    dwn_area, 
                    btn_reset,
                    btn_NewStaff
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            staff
        ],
        alignment=ft.MainAxisAlignment.START,
        width=1450,
    )
    

    content = ft.Container(
        content=content_staff
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