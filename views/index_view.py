import flet as ft

from views.products.product import ProductsView
from views.shipments.shipment import ShipmentView
from views.orders.order import OrderView


def change_view(index, page):
    views = {
        0: ProductsView(page),
        1: OrderView(page),
        2: ShipmentView(page),
    }
    return views[index]


def IndexView(page):
    view = ft.Container(content=change_view(0, page))

    def navRail(e):
        view.content = change_view(e.control.selected_index, page)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.NOTE_ALT_OUTLINED, 
                selected_icon=ft.icons.NOTE_ALT, 
                label="Compras", 
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.STICKY_NOTE_2_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.STICKY_NOTE_2),
                label="Ordenes",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.LOCAL_SHIPPING_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.LOCAL_SHIPPING),
                label="Envios",
            ),
        ],
        on_change=navRail,
    )

    content = ft.Column(
        [  
            ft.Row(
                [
                    rail,
                    view
                ], 
                alignment=ft.MainAxisAlignment.START,
                height=700
            )
        ]
    )

    return content


if __name__ == '__main__':
    IndexView()