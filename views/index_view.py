import flet as ft

from views.products.product import ProductsView
from views.shipments.shipment import ShipmentView


def IndexView(page):
    views = {
        0: ProductsView(page),
        1: ShipmentView(page)
    }
    view = ft.Container(content=views[0])

    def navRail(e):
        view.content = views[e.control.selected_index]
        # content.update()
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
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First", 
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            )
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