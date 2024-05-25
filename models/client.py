from peewee import *
from models.connectionDB import BaseModel


# Definición de los campos o columnas (Field instances)
class client(BaseModel):
    cli_id = IntegerField(primary_key=True)
    cli_name = CharField(50)
    cli_phone = CharField(10)
    cli_email = CharField(30)
    cli_address = CharField(200)


def post_client(name, phone, email, address) -> None:
    client.create(
        cli_name=name,
        cli_phone=phone,
        cli_email=email,
        cli_address=address
    )
    print('Client created successfully')


def get_clients() -> list:
    return client.select()

def get_client_by_name(name: str) -> list:
    return client.select().where(client.cli_name.contains(name))


def delete_client_by_id(id: int) -> None:
    client.delete().where(client.cli_id == id).execute()