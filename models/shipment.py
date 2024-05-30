from peewee import *
from models.connectionDB import BaseModel
from models.staff import staff


# Definición de los campos o columnas (Field instances)
class shipment(BaseModel):
    shi_id = AutoField()
    shi_date = DateField()
    shi_no_orders = IntegerField()
    shi_carrier_id = ForeignKeyField(staff)


def post_shipment(date, no_orders, carrier_id):
    shipment.create(
        shi_date=date,
        shi_no_orders=no_orders,
        shi_carrier_id=carrier_id
    )
    return get_last_shipment()

def get_last_shipment():
    query = shipment.select(shipment.shi_id).order_by(shipment.shi_id.desc()).limit(1)
    return query[0].shi_id

def get_shipment_by_id(id:int):
    data = (shipment.select(shipment, staff.sta_name, staff.sta_last_name)
            .join(staff, on=(staff.sta_id == shipment.shi_carrier_id), attr='s')
            .where(shipment.shi_id == id))
    return data[0]

def get_shipments():
    return (shipment.select(shipment, staff.sta_name, staff.sta_last_name)
            .join(staff, on=(staff.sta_id == shipment.shi_carrier_id), attr='s'))

def delete_shipment(id:int):
    shipment.delete().where(shipment.shi_id == id).execute()
    return

def get_shipments_by_date(order_by:str):
    if order_by == 'Más reciente':
        return (shipment.select(shipment, staff.sta_name, staff.sta_last_name)
            .join(staff, on=(staff.sta_id == shipment.shi_carrier_id), attr='s')
            .order_by(shipment.shi_date.desc()))
    if order_by == 'Más antigua':
        return (shipment.select(shipment, staff.sta_name, staff.sta_last_name)
            .join(staff, on=(staff.sta_id == shipment.shi_carrier_id), attr='s')
            .order_by(shipment.shi_date.asc()))