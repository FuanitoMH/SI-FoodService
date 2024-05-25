import flet as ft

def nav_view(page):

    color_text = ft.colors.WHITE if page.theme_mode == "dark" else ft.colors.BLACK

    btn_home_view = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.HOME_OUTLINED, color=color_text),
                    ft.Text(value="Inicio", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/home')
        )
    btn_product_view = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.NOTE_ALT_OUTLINED, color=color_text),
                    ft.Text(value="Productos", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/products')
        )
    btn_view_order = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.STICKY_NOTE_2_OUTLINED, color=color_text),
                    ft.Text(value="Ordenes", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/orders')
        )
    btn_view_shipment = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.LOCAL_SHIPPING_OUTLINED, color=color_text ),
                    ft.Text(value="Envios", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/shipments')
        )
    
    btn_view_client = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.GROUPS_OUTLINED, color=color_text ),
                    ft.Text(value="Cientes", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/clients')
        )

    btn_view_staff = ft.TextButton(
            width=100,
            content=ft.Column(
                [
                    ft.Icon(name=ft.icons.EMOJI_PEOPLE_OUTLINED, color=color_text ),
                    ft.Text(value="R.H.", color=color_text),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: page.go('/staff')
        )
    nav = ft.Column(
        controls=[
            btn_home_view,
            btn_product_view,
            btn_view_client,
            btn_view_staff,
            btn_view_order,
            btn_view_shipment,
        ], 
        alignment=ft.MainAxisAlignment.START,
    )

    return nav