import flet as ft
from peewee import *
from connectionDB import BaseModel


class staff(BaseModel):
    # Definición de los campos o columnas (Field instances)
    sta_id = IntegerField(primary_key=True)
    sta_name = CharField(60)
    sta_phone = CharField(10)
    sta_email = CharField(30, unique=True)
    sta_rool = CharField(20)
    sta_password = CharField(8)


def addStaff (name, phone, email, rool, pw) -> None:
    staff.create(
        sta_name = name,
        sta_phone = phone,
        sta_email = email,
        sta_rool = rool,
        sta_password = pw
    )
    print('Staff added')

def logginStaff(email, pw):
    return staff.select().where((staff.sta_email == email )&(staff.sta_password == pw))
       

if __name__ == '__main__':
    addStaff()
    