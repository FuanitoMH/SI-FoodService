import flet as ft

# views
from views.home_view import HomeView
from views.profile.profile_view import ProfileView
from views.settings.settings_view import SettingsView
from views.loggin.loggin_view import logginView

# views Staff
from views.staff.staff import StaffView
from views.staff.staff_register import registerStaffView

# views Departments
from views.products.product import ProductsView
from views.products.product_register import ProductsRegisterView
from views.clients.client import ClientView
from views.clients.client_register import ClientsRegisterView
from views.orders.order import OrdersView
from views.shipments.shipment import ShipmentView

def myRutes(page: ft.Page, ruta: str):
    routes = {
        "/home": HomeView(page),
        "/profile": ProfileView(page),
        "/settings": SettingsView(page),
        "/staff": StaffView(page),
        "/staff/register": registerStaffView(page),
        "/login": logginView(page),
        "/products": ProductsView(page),
        "/products/register": ProductsRegisterView(page),
        "/clients": ClientView(page),
        "/clients/register": ClientsRegisterView(page),
        "/orders": OrdersView(page),
        "/shipments": ShipmentView(page),
    }
    return routes[ruta]


class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.body = ft.Container(content=myRutes(page, "/home"))

    def route_change(self, route):
        print('current rute: ', route.route)
        self.body.content = myRutes(self.page, route.route)
        self.body.update()
