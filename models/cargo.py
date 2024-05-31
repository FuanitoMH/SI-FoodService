from peewee import *
import mysql.connector

from models.connectionDB import BaseModel
from models.order import order
from models.client import Client
from models.shipment import shipment


# Definición de los campos o columnas (Field instances)
class cargo(BaseModel):
    car_ord_id = ForeignKeyField(order)
    car_shi_id = ForeignKeyField(shipment)


def post_cargo(ord_id, shi_id) -> None:
    cargo.create(
        car_ord_id=ord_id,
        car_shi_id=shi_id
    )



def connDB():
    try:
        # Establish a connection
        conn = mysql.connector.connect(
            user="root", 
            password="pass", 
            host="localhost", 
            database="foodservice")
        print("Connection established")
    except Exception as e:
        raise Exception(e)

    return conn

def get_orders_by_id_shipment(shi_id:int) -> list:
    conn = connDB()
    cursor = conn.cursor()
    cursor.execute(f'SELECT Client.cli_name, Client.cli_address, order.ord_status, order.ord_id  FROM cargo JOIN `order` ON cargo.car_ord_id = `order`.ord_id JOIN client ON `order`.ord_cli_id = client.cli_id WHERE car_shi_id = {shi_id}')

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_orders_status_onway_by_shiID(shi_id:int) -> None:
    conn = connDB()
    cursor = conn.cursor()
    cursor.execute(f'UPDATE `order` SET ord_status = "en camino" WHERE ord_id IN (SELECT car_ord_id FROM cargo WHERE car_shi_id = {shi_id})')
    conn.commit()
    cursor.close()
    conn.close()