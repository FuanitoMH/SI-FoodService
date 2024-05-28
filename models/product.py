from peewee import *
from models.connectionDB import BaseModel


class product(BaseModel):
    # Definición de los campos o columnas (Field instances)
    pro_id = IntegerField(primary_key=True)
    pro_name = CharField(60)
    pro_description = CharField(200)
    pro_stock = IntegerField()
    pro_category = CharField(20)
    pro_temperature = CharField(20)
    pro_sup_id = IntegerField()


def post_product (name, description, stock, category, temperature, sup_id) -> None:
    product.create(
        pro_name = name,
        pro_description = description,
        pro_stock = stock,
        pro_category = category,
        pro_temperature = temperature,
        pro_sup_id = sup_id
    )
    print('Product created successfully')

def get_products() -> list:
    return product.select()

def get_product_by_id(id: int) -> list:
    return product.select().where(product.sta_id == id)

def get_product_by_name(name: str) -> list:
    return product.select().where(product.pro_name.contains(name))

def get_product_by_category(category: str) -> list:
    return product.select().where(product.pro_category == category)

def get_product_by_temperature(temperature: str) -> list:
    return product.select().where(product.pro_temperature == temperature)
       
def delete_product_by_id(id: int) -> None:
    product.delete().where(product.pro_id == id).execute()
    
def get_name_products():
    return product.select(product.pro_id, product.pro_name)