import flet as ft
from models.product import get_products, get_product_by_category, get_product_by_temperature, get_product_by_name, delete_product_by_id
from user_controls.alert_dialog import AlertDialog
from user_controls.app_nav import nav_view




def ProductsView(page):
    # NAVIGATION
    nav = nav_view(page)


    # -- CONTROLS --
    alert_dialog = AlertDialog(page)
    text_search = ft.TextField(icon=ft.icons.SEARCH, width=600, label='Buscar', border= 'UNDERLINE', border_color=ft.colors.WHITE)
    btn_search = ft.ElevatedButton(text='Reset', icon=ft.icons.RESTART_ALT, icon_color='#9AC8CD', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
    btn_NewProduct = ft.ElevatedButton( "Nuevo Producto", color=ft.colors.WHITE, width=110, bgcolor=ft.colors.GREEN)

    dwn_Category = ft.Dropdown(label='Categoria', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                                ft.dropdown.Option("Todos"),
                                ft.dropdown.Option("bebida"),
                                ft.dropdown.Option("comida"),
                                ft.dropdown.Option("acompañamiento"),
                            ])
    dwn_Temperature = ft.Dropdown(label='Temperatura', bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=140, border='none', text_size=15,
                        options=[
                            ft.dropdown.Option("Todos"),
                            ft.dropdown.Option("seco"),
                            ft.dropdown.Option("refrigerado"),
                            ft.dropdown.Option("congelado"),
                            ]
                        )

    def delete_product(e: ft.ControlEvent):
        delete_product_by_id(e.control.tooltip)
        data_products = get_products()
        list_products = []
        list_products = draw_products(data_products)
        container_Products.controls = list_products
        page.update()
        alert_dialog.show('Producto eliminado', 'El producto ha sido eliminado correctamente', status='info')
    
    def draw_products(data_products):
        products = []
        bgColorCard = ft.colors.GREY_900 if page.theme_mode == "dark" else ft.colors.GREY_100
        bgColorStock = '#222831'
        txColorStock = '#EEEEEE'
        bgColorCategory  = '#352F44'
        txtColorCategory = '#B9B4C7'
        bgColorTemperature  = '#6096B4'
        txtColorTemperature = '#E9E8E8'
        for product in data_products:
            products.append(
                ft.Container(
                        content=ft.Column(
                            [   
                                ft.Row(
                                    [
                                        ft.Text(value=product.pro_name.upper(), size=20, width=200, text_align=ft.TextAlign.CENTER),
                                        ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED, icon_color="pink600", icon_size=20,
                                                    tooltip=product.pro_id, on_click=lambda e: delete_product(e)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Text(value=product.pro_description, size=15),
                                ft.Row(
                                    [
                                        ft.Text(value='Existencias: ', size=15),
                                        ft.Container(content=ft.Text(value=product.pro_stock, size=15, color=txColorStock, text_align=ft.TextAlign.CENTER), 
                                                    border_radius=10, bgcolor=bgColorStock, width=25),
                                    ]
                                )
                                ,
                                ft.Row(
                                    [
                                        ft.Container(content= ft.Text(value=product.pro_category, size=15, color=txtColorCategory, text_align=ft.TextAlign.CENTER), 
                                                    border_radius=10, bgcolor=bgColorCategory, width=120),
                                        ft.Container(content=ft.Text(value=product.pro_temperature, size=15, color=txtColorTemperature, text_align=ft.TextAlign.CENTER),
                                                    border_radius=10, bgcolor=bgColorTemperature, width=90),
                                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                                ft.Text(value=product.pro_sup_id, size=15),
                            ]
                        ),
                        width=270,
                        height=200,
                        padding=10,
                        bgcolor=bgColorCard, 
                        border_radius=ft.border_radius.all(5),
                )
            )
        return products
    

    # -- VARIABLES --
    list_products = []
    data_products = get_products()
    list_products = draw_products(data_products)


    container_Products = ft.Row(controls=list_products,
                        wrap=True,
                        scroll='HIDDEN',
                        # expand=True,
                        height=600,
                        width=1410,
                        run_spacing=10,
                    )

    # -- FUNCTIONS --
    def serach_by_category(e: ft.ControlEvent):
        data_products = get_product_by_category(dwn_Category.value) if dwn_Category.value != 'Todos' else get_products()
        list_products = []
        list_products = draw_products(data_products)
        container_Products.controls = list_products
        text_search.value = ''
        dwn_Temperature.value = ''
        page.update()
    
    def serach_by_temperature(e: ft.ControlEvent):
        data_products = get_product_by_temperature(dwn_Temperature.value) if dwn_Temperature.value != 'Todos' else get_products()
        list_products = []
        list_products = draw_products(data_products)
        container_Products.controls = list_products
        text_search.value = ''
        dwn_Category.value = ''
        page.update()
    
    def search_all_products(e: ft.ControlEvent):
        data_products = get_products()
        list_products = []
        list_products = draw_products(data_products)
        container_Products.controls = list_products
        text_search.value = ''
        dwn_Category.value = ''
        dwn_Temperature.value = ''
        page.update()

    def search_by_name(e: ft.ControlEvent):
        data_products = get_product_by_name(text_search.value)
        list_products = []
        list_products = draw_products(data_products)
        container_Products.controls = list_products
        dwn_Category.value = ''
        dwn_Temperature.value = ''
        page.update()

    

    # -- EVENTS --
    btn_NewProduct.on_click = lambda e: page.go('/products/register')
    dwn_Category.on_change = serach_by_category
    dwn_Temperature.on_change = serach_by_temperature
    btn_search.on_click = search_by_name
    text_search.on_change = search_by_name
    btn_search.on_click = search_all_products

    content = ft.Column(
            [
                ft.Row(
                    [   
                        text_search,
                        btn_search,
                        dwn_Category, 
                        dwn_Temperature,
                        btn_NewProduct
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
                container_Products
            ],
            alignment=ft.MainAxisAlignment.START,
            width=1450,
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
