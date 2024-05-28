from peewee import *
from models.connectionDB import BaseModel
from models.client import Client


# Definición de los campos o columnas (Field instances)
class order(BaseModel):
    ord_id = AutoField()
    ord_cli_id = ForeignKeyField(Client, backref='orders')
    ord_date = DateField()
    ord_status = CharField(20)

def get_last_order_id():
    query = order.select(order.ord_id).order_by(order.ord_id.desc()).limit(1)
    return query[0].ord_id

def post_order(cli_id, date, status) -> None:
    order.create(
        ord_cli_id=cli_id,
        ord_date=date,
        ord_status=status
    )
    print(get_last_order_id())
    return get_last_order_id()


def get_orders() -> list:
    return order.select()

def get_order_join_client():
    return order.select(order, Client).join( Client, on=(order.ord_cli_id == Client.cli_id), attr='c')

def get_order_join_client_by_id(id: int):
    return order.select(order, Client).join( Client, on=(order.ord_cli_id == Client.cli_id), attr='c').where(order.ord_id == id)
    
def get_order_by_date(order_by: str) -> list:
    if order_by == 'Más reciente':
        return order.select(order, Client).join( Client, on=(order.ord_cli_id == Client.cli_id), attr='c').order_by(order.ord_date.desc())
    if order_by == 'Más antigua':
        return order.select(order, Client).join( Client, on=(order.ord_cli_id == Client.cli_id), attr='c').order_by(order.ord_date.asc())

def get_orders_by_status(status: str) -> list:
    return order.select(order, Client).join( Client, on=(order.ord_cli_id == Client.cli_id), attr='c').where(order.ord_status == status)

if __name__ == '__main__':
    data = get_order_join_client()
    for d in data:
        print(d.cli_name, d.ord_date, d.ord_status, d.ord_cli_id.cli_phone, d.ord_cli_id.cli_email, d.ord_cli_id.cli_address)