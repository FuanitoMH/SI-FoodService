import flet as ft


# Class to show an alert dialog
class AlertDialog:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dialog = ft.AlertDialog()

    def show(self, title: str, content: str, status: str = 'info'):
        self.page.dialog = self.dialog

        if status == 'info':
            ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK)
            self.dialog.icon = ft.Icon(name=ft.icons.INFO)
            self.dialog.bgcolor = ft.colors.BLUE_200
        elif status == 'error':
            self.dialog.icon = ft.Icon(name=ft.icons.ERROR)
            self.dialog.bgcolor = ft.colors.RED
        elif status == 'success':
            self.dialog.icon = ft.Icon(name=ft.icons.CHECK)
            self.dialog.bgcolor = ft.colors.GREEN
        elif status == 'warning':
            self.dialog.icon = ft.Icon(name=ft.icons.WARNING)
            self.dialog.bgcolor = ft.colors.YELLOW

        self.dialog.title = ft.Text(f'{title}', size=22, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
        self.dialog.content = ft.Text(f'{content}', size=15, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
        self.dialog.open = True
        self.page.update()
