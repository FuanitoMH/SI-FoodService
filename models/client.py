from peewee import *
import mysql.connector
from models.connectionDB import BaseModel


# Definición de los campos o columnas (Field instances)
class Client(BaseModel):
    # cli_id = IntegerField(primary_key=True)
    cli_id = AutoField()
    cli_name = CharField(50)
    cli_phone = CharField(10)
    cli_email = CharField(30)
    cli_address = CharField(200)


def post_client(name, phone, email, address) -> None:
    Client.create(
        cli_name=name,
        cli_phone=phone,
        cli_email=email,
        cli_address=address
    )
    print('Client created successfully')


def get_clients() -> list:
    return Client.select()

def get_client_by_id(id: int):
    return Client.select().where(Client.cli_id == id)

def get_client_by_name(name: str) -> list:
    return Client.select().where(Client.cli_name.contains(name))

def delete_client_by_id(id: int) -> None:
    Client.delete().where(Client.cli_id == id).execute()


# Querys for orders
def get_name_clients():
    return Client.select(Client.cli_id, Client.cli_name)

def get_one_client_by_id(id: int):
    data = Client.select().where(Client.cli_id == id)
    return data[0]


# def connDB():
#     try:
#         # Establish a connection
#         conn = mysql.connector.connect(
#             user="root", 
#             password="pass", 
#             host="localhost", 
#             database="foodservice")
#         print("Connection established")
#     except Exception as e:
#         raise Exception(e)

#     return conn

# def get_clients_(shi_id:int) -> list:
#     conn = connDB()
#     cursor = conn.cursor()
#     cursor.execute(f'SELECT Client, COUNT(ord_cli_id) AS no_orders
#     FROM `order`
#     JOIN client
#         ON order.ord_cli_id = client.cli_id
#     GROUP BY cli_name;')

#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return data