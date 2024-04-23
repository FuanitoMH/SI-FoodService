import flet as ft

# views
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView
from views.loggin_view import logginView

# views Staff
from views.RegisterStaff_view import registerStaffView


def myRutes(page: ft.Page, ruta: str):
    routes = {
        "/home": IndexView(page),
        "/profile": ProfileView(page),
        "/settings": SettingsView(page),
        "/staff": registerStaffView(page),
        "/login": logginView(page)
    }
    return routes[ruta]


class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.body = ft.Container(content=myRutes(page, "/home"))

    def route_change(self, route):
        print('rute: ', route.route)
        # self.body.content = self.routes[route.route]
        self.body.content = myRutes(self.page, route.route)
        self.body.update()
