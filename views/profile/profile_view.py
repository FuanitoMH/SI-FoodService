import flet as ft

from models.staff import *

def ProfileView(page):
    txt_name = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
    txt_phone = ft.Text("", size=20)
    txt_email = ft.Text("", size=20)
    txt_area = ft.Text("", size=20)

    session = page.client_storage.get('session')
    print(session, '/profile')

    query = get_staff_by_id(session)
    for staff in query:
        txt_name.value = f"{staff.sta_name} {staff.sta_last_name}"
        txt_phone.value = staff.sta_phone
        txt_email.value = staff.sta_email
        txt_area.value = staff.sta_area
        


    
    content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("My Profile", size=30), 
                        ft.IconButton(icon=ft.icons.PERSON_ROUNDED, icon_size=30),
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.FACE_OUTLINED, color=ft.colors.BLUE, size=150),
                        ft.Column(
                            [
                                txt_name,
                                ft.Row([
                                    ft.Icon(name=ft.icons.EMAIL_OUTLINED, color=ft.colors.ORANGE, size=20),
                                    txt_email,
                                ]),
                                ft.Row([
                                    ft.Icon(name=ft.icons.PHONE_OUTLINED, color=ft.colors.ORANGE, size=20),
                                    txt_phone,
                                ]),
                                ft.Row([
                                    ft.Icon(name=ft.icons.LOCATION_HISTORY_OUTLINED, color=ft.colors.ORANGE, size=20),
                                    txt_area,
                                ])
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
            ],
            spacing=50
        )
    
    return content

if __name__ == "__main__":
    ProfileView(ft.Page())