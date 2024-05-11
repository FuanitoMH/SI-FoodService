import flet as ft
from peewee import *
from connectionDB import BaseModel


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

def get_products():
    return product.select()

def get_product_by_id(id: int):
    return product.select().where(product.sta_id == id)
       

if __name__ == '__main__':
    post_product()