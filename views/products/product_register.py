import flet as ft
from models.product import get_products, post_product
from user_controls.alert_dialog import AlertDialog
from user_controls.app_nav import nav_view


def ProductsRegisterView(page: ft.Page):
    # NAVIGATION
    nav: ft.Column = nav_view(page) 

    alert = AlertDialog(page)

    # -- CONTROLS --
    text_name = ft.TextField(label='Nombre', width=500, border='UNDERLINE', text_size=15)
    text_description = ft.TextField(label='Descripción', width=500, height=200, border='none', text_size=15, multiline=True)
    number_stock = ft.TextField(label='Existencias', width=160, border='UNDERLINE', input_filter=ft.NumbersOnlyInputFilter(), text_size=15)
    pro_sup_id = ft.TextField(label='ID proveedor', width=500, border='UNDERLINE', text_size=15)

    dwn_category = ft.Dropdown(label='Categoria', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=160, border='none', text_size=15,
        options=[
                ft.dropdown.Option("bebida"),
                ft.dropdown.Option("comida"),
                ft.dropdown.Option("acompañamiento"),
            ])
    dwn_Temperature = ft.Dropdown(label='Temperatura', bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, width=160, border='none', text_size=15,
        options=[
            ft.dropdown.Option("seco"),
            ft.dropdown.Option("refrigerado"),
            ft.dropdown.Option("congelado"),
            ]
        )
    
    btn_cancel = ft.ElevatedButton('Cancelar', color=ft.colors.WHITE, on_click=lambda e: cancel(e), bgcolor=ft.colors.RED)
    btn_register = ft.ElevatedButton('Agregar', color=ft.colors.WHITE, on_click=lambda e: add_product(e), bgcolor=ft.colors.GREEN)

    # -- FUNCTIONS --
    def add_product(e: ft.ControlEvent):
        if not validate_inputs():
            alert.show(title="Error", content="Todos los campos son requeridos", status="error")
            clean_fields()
            return

        post_product(text_name.value, text_description.value, number_stock.value, dwn_category.value, dwn_Temperature.value, pro_sup_id.value)
        alert.show(title="Éxito", content="Producto registrado", status="success")
        page.go('/products')

    def cancel(e: ft.ControlEvent):
        page.go('/products')
    
    def validate_inputs():
        if all([text_name.value, text_description.value, number_stock.value, dwn_category.value, dwn_Temperature.value, pro_sup_id.value]):
            return True
        return False
    
    def clean_fields():
        text_name.value = ''
        text_description.value = ''
        number_stock.value = ''
        dwn_category.value = ''
        dwn_Temperature.value = ''
        pro_sup_id.value = ''
        page.update()


    # -- EVENTS --
    text_name.on_change = validate_inputs
    text_description.on_change = validate_inputs
    number_stock.on_change = validate_inputs
    pro_sup_id.on_change = validate_inputs
    dwn_category.on_change = validate_inputs
    dwn_Temperature.on_change = validate_inputs



    # -- CONTENT --
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=ft.colors.RED, on_click=lambda e: page.go('/products'))
                ],
                width=500,
                alignment=ft.MainAxisAlignment.END
            ),
            ft.Text("Registrar Producto", size=20),
            text_name,
            text_description,
            ft.Row(
                [
                    number_stock,
                    dwn_category,
                    dwn_Temperature
                ], 
                width=500,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            pro_sup_id,
            ft.Row(
                [
                    btn_cancel,
                    btn_register
                ],
                alignment=ft.MainAxisAlignment.END,
                width=500
            )
        ],
        width=1400,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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

