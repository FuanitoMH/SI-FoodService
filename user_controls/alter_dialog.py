import flet as ft


# Class to show an alert dialog
class AlertDialog:
    def __init__(self, page: ft.Page, title: str, content: str):
        self.page = page
        self.dialog = ft.AlertDialog(
                    title   = ft.Text(f'{title}', size=22, color=ft.colors.RED, text_align=ft.TextAlign.CENTER),
                    content = ft.Text(f'{content}', size=12)
                )
        self.page.dialog = self.dialog

    def show(self):
        self.dialog.open = True
        self.page.update()
