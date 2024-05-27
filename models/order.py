from peewee import *
from models.connectionDB import BaseModel
from models.client import Client


# Definición de los campos o columnas (Field instances)
class Order(BaseModel):
    ord_id = AutoField()
    ord_cli_id = ForeignKeyField(Client, backref='orders')
    ord_date = DateField()
    ord_status = CharField(20)


def post_order(cli_id, date, status) -> None:
    Order.create(
        ord_cli_id=cli_id,
        ord_date=date,
        ord_status=status
    )
    print('Client created successfully')

def get_orders() -> list:
    return Order.select()

def get_order_join_client():
    return Order.select(Order, Client).join( Client, on=(Order.ord_cli_id == Client.cli_id), attr='c')
    

if __name__ == '__main__':
    data = get_order_join_client()
    for d in data:
        print(d.cli_name, d.ord_date, d.ord_status, d.ord_cli_id.cli_phone, d.ord_cli_id.cli_email, d.ord_cli_id.cli_address)