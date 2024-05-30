import flet as ft
from peewee import *
from models.connectionDB import BaseModel


class staff(BaseModel):
    # Definición de los campos o columnas (Field instances)
    sta_id = IntegerField(primary_key=True)
    sta_name = CharField(60)
    sta_last_name = CharField(60)
    sta_phone = CharField(10)
    sta_email = CharField(30, unique=True)
    sta_area = CharField(20)
    sta_password = CharField(8)


def addStaff (name, last_name, phone, email, area, pw) -> None:
    staff.create(
        sta_name = name,
        sta_last_name = last_name,
        sta_phone = phone,
        sta_email = email,
        sta_area = area,
        sta_password = pw
    )
    print('Staff added')

def logginStaff(email, pw):
    return staff.select().where((staff.sta_email == email )&(staff.sta_password == pw))

def get_staff() -> list:
    return staff.select()

def get_staff_by_id(id: int) -> list:
    return staff.select().where(staff.sta_id == id)

def get_staff_by_name(name: str) -> list:
    return staff.select().where((staff.sta_name.contains(name)) | (staff.sta_last_name.contains(name)))

def get_staff_by_area(area: str) -> list:
    return staff.select().where(staff.sta_area == area)

def delete_staff_by_id(id: int) -> None:
    staff.delete().where(staff.sta_id == id).execute()
    print('Staff deleted successfully')
    return

def update_staff(id: int, name: str, last_name: str, phone: str, email: str, area: str, pw: str) -> None:
    staff.update(
        sta_name = name,
        sta_last_name = last_name,
        sta_phone = phone,
        sta_email = email,
        sta_area = area,
        sta_password = pw
    ).where(staff.sta_id == id).execute()
    print('Staff updated successfully')

def get_name_carriers():
    return staff.select(staff.sta_id, staff.sta_name, staff.sta_last_name).where(staff.sta_area == 'transportista')
    

if __name__ == '__main__':
    addStaff()
    