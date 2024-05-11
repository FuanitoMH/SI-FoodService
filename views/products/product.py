import flet as ft
from models.product import get_products
from user_controls.alert_dialog import AlertDialog
from views.products.modal_product import ProductModal

def ProductsView(page):
    # -- FUNCTIONS --
    def open_modal(e: ft.ControlEvent):
        product_modal.show()

    # -- CONTROLS --
    product_modal = ProductModal(page)
    alert_dialog = AlertDialog(page)
    text_search = ft.TextField(icon=ft.icons.SEARCH, width=700, label='Buscar', border= 'UNDERLINE', border_color=ft.colors.WHITE)
    btn_All = ft.ElevatedButton("All", color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
    btn_NewProduct = ft.ElevatedButton( "Nuevo Producto", color=ft.colors.WHITE, width=120, bgcolor=ft.colors.GREEN)

    dwn_Category = ft.Dropdown(label='Categoria', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("All"),
                                ft.dropdown.Option("bebida"),
                                ft.dropdown.Option("comida"),
                                ft.dropdown.Option("acompañamiento"),
                            ])
    dwn_Temperature = ft.Dropdown(label='Temperatura', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                            ft.dropdown.Option("All"),
                            ft.dropdown.Option("seco"),
                            ft.dropdown.Option("refrigerado"),
                            ft.dropdown.Option("congelado"),
                            ]
                        )
    
    
    btn_NewProduct.on_click = open_modal

    # -- PRODUCTS --
    bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
    cardProduct = content=ft.Container(
                    content=ft.Text(value="pro"),
                    alignment=ft.alignment.center,
                    width=270,
                    height=200,
                    bgcolor=bgColorCard,
                    border_radius=ft.border_radius.all(5),
                )
    
    data_products = get_products() # get data from database
    list_products = []
    for product in data_products:
        list_products.append(
            ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value=product.pro_name, size=20),
                            ft.Text(value=product.pro_description, size=15),
                            ft.Text(value=product.pro_stock, size=15),
                            ft.Text(value=product.pro_category, size=15),
                            ft.Text(value=product.pro_sup_id, size=15),
                        ]
                    ),
                    alignment=ft.alignment.center,
                    width=270,
                    height=200,
                    bgcolor=bgColorCard,
                    border_radius=ft.border_radius.all(5),
            )
        )
 
    contProducts = ft.Row(controls=list_products,
                        wrap=True,
                        scroll='HIDDEN',
                        # expand=True,
                        height=600,
                        width=1410,
                        run_spacing=10,
                    )

    content = ft.Column(
            [
                ft.Row(
                    [   
                        text_search,
                        btn_All,
                        dwn_Category, 
                        dwn_Temperature,
                        btn_NewProduct
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
                contProducts
            ],
            alignment=ft.MainAxisAlignment.START,
            width=1500,
        )
    
    
    return content
