import flet as ft
from models.product import post_product
from user_controls.alert_dialog import AlertDialog



# Class to show modal dialog
class ProductModal:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dlg_modal = ft.AlertDialog()
        self.text_name = ft.TextField(label='Nombre', width=500, border='UNDERLINE', text_size=15)
        self.text_description = ft.TextField(label='Descripción', width=500, height=100, border='none', text_size=15, multiline=True)
        self.number_stock = ft.TextField(label='Existencias', width=500, border='UNDERLINE', input_filter=ft.NumbersOnlyInputFilter(), text_size=15)
        self.pro_sup_id = ft.TextField(label='ID proveedor', width=500, border='UNDERLINE', text_size=15)

        self.dwn_category = ft.Dropdown(label='Categoria', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=110, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("bebida"),
                                ft.dropdown.Option("comida"),
                                ft.dropdown.Option("acompañamiento"),
                            ])
        self.dwn_Temperature = ft.Dropdown(label='Temperatura', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=110, border='none', text_size=15,
                        options=[
                            ft.dropdown.Option("seco"),
                            ft.dropdown.Option("refrigerado"),
                            ft.dropdown.Option("congelado"),
                            ]
                        )


    def close(self, e: ft.ControlEvent):
        self.dlg_modal.open = False
        self.clean_fields()
        self.page.update()

    def clean_fields(self):
        self.text_name.value = ''
        self.text_description.value = ''
        self.number_stock.value = ''
        self.dwn_category.value = ''
        self.dwn_Temperature.value = ''
        self.pro_sup_id.value = ''
        self.page.update()
    
    def add_product(self, e: ft.ControlEvent):
        alert_dialog = AlertDialog(self.page)
        self.dlg_modal.open = False
        if all([self.text_name.value, self.text_description.value, self.number_stock.value, self.dwn_category.value, self.dwn_Temperature.value, self.pro_sup_id.value]):
            post_product(
            self.text_name.value,
            self.text_description.value,
            self.number_stock.value,
            self.dwn_category.value,
            self.dwn_Temperature.value,
            self.pro_sup_id.value
        )
            self.clean_fields()
            alert_dialog.show(title="SUCCESS", content="Producto registrado", status="success")
            # self.page.go('/home')
            self.page.go('/products')
            self.page.update()
        else:        
            alert_dialog.show(title="ERROR", content="Todos los campos son requeridos", status="error")
            self.clean_fields()
            self.page.update()
    

    def show(self, title:str='Agregar producto'):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.content_padding = 10

        self.dlg_modal.title = ft.Text(f'{title}', size=22, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
        self.dlg_modal.content = ft.Column(
            controls=[
                self.text_name,
                self.text_description,
                self.number_stock,
                ft.Row(
                    [
                        self.dwn_category,
                        self.dwn_Temperature
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                self.pro_sup_id
            ]
        )
        self.dlg_modal.actions = [
            ft.ElevatedButton('Cancelar', color=ft.colors.BLACK87, on_click=lambda e: self.close(e), bgcolor=ft.colors.WHITE60),
            ft.ElevatedButton('Agregar', color=ft.colors.WHITE, on_click=lambda e: self.add_product(e), bgcolor=ft.colors.GREEN)
            ]
        self.dlg_modal.actions_alignment = ft.MainAxisAlignment.END
        self.dlg_modal.open = True
        self.page.update()
