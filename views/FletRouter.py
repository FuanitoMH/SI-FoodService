import flet as ft

# views
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView

from views.RegisterStaff_view import registerStaffView
from views.loggin_view import logginView


class Router:

    def __init__(self, page):
        self.page = page
        self.routes = {
            "/": IndexView(page),
            "/profile": ProfileView(page),
            "/settings": SettingsView(page),
            "/staff": registerStaffView(page),
            "/loggin": logginView(page)
        }
        self.body = ft.Container(content=self.routes['/loggin'])

    def route_change(self, route):
        print(route)
        self.body.content = self.routes[route.route]
        self.body.update()
