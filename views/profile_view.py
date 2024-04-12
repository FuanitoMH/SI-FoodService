import flet as ft

from models.staff import *

def ProfileView(page):
    nameUser = ft.Text("", size=25)
    phoneUser = ft.Text("", size=25)
    emailUser = ft.Text("", size=25)

    session = page.client_storage.get('session')
    print(session, '/profile')

    query = getStaffById(session)
    for staff in query:
        nameUser.value = staff.sta_name
        phoneUser.value = staff.sta_phone
        emailUser.value = staff.sta_email


    
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
                        ft.Image(src=f"/banner.png", width=200, border_radius=100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        nameUser
                    ],
                ),
                ft.Row(
                    [
                        phoneUser
                    ]
                ),
                ft.Row(
                    [
                        emailUser
                    ]
                )

            ]
        )
    
    return content
