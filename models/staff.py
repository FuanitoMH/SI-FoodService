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
    sta_rool = CharField(20)
    sta_password = CharField(8)


def addStaff (name, last_name, phone, email, rool, pw) -> None:
    staff.create(
        sta_name = name,
        sta_last_name = last_name,
        sta_phone = phone,
        sta_email = email,
        sta_rool = rool,
        sta_password = pw
    )
    print('Staff added')

def logginStaff(email, pw):
    return staff.select().where((staff.sta_email == email )&(staff.sta_password == pw))

def getStaffById(id: int):
    return staff.select().where(staff.sta_id == id)
       

if __name__ == '__main__':
    addStaff()
    