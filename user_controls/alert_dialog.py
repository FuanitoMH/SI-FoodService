import flet as ft


# Class to show an alert dialog
class AlertDialog:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dialog = ft.AlertDialog()

    def close(self, e: ft.ControlEvent):
        self.dialog.open = False
        self.page.update()

    def show(self, title: str, content: str, status: str = 'info'):
        self.page.dialog = self.dialog

        if status == 'info':
            self.dialog.icon = ft.Icon(name=ft.icons.INFO, color=ft.colors.BLACK87)
            self.dialog.bgcolor = ft.colors.BLUE_200
        elif status == 'error':
            self.dialog.icon = ft.Icon(name=ft.icons.ERROR, color=ft.colors.BLACK87)
            self.dialog.bgcolor = ft.colors.RED
        elif status == 'success':
            self.dialog.icon = ft.Icon(name=ft.icons.CHECK, color=ft.colors.BLACK87)
            self.dialog.bgcolor = ft.colors.GREEN
        elif status == 'warning':
            self.dialog.icon = ft.Icon(name=ft.icons.WARNING, color=ft.colors.BLACK87)
            self.dialog.bgcolor = ft.colors.YELLOW_ACCENT_700

        self.dialog.icon.size = 45
        self.dialog.title = ft.Text(f'{title}', size=22, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
        self.dialog.content = ft.Text(f'{content}', size=15, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
        self.dialog.actions = [ft.ElevatedButton('Aceptar', color=ft.colors.BLACK87, on_click=lambda e: self.close(e), bgcolor=ft.colors.WHITE60)]
        self.dialog.actions_alignment = ft.MainAxisAlignment.END
        self.dialog.open = True
        self.page.update()
