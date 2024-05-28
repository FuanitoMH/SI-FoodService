from peewee import *
from models.connectionDB import BaseModel
from models.product import product
from models.order import order


# Definición de los campos o columnas (Field instances)
class orderitems(BaseModel):
    itm_ord_id = IntegerField()
    itm_pro_id = IntegerField()
    itm_stock = IntegerField()


def post_item(ord_id, pro_id, stock) -> None:
    orderitems.create(
        itm_ord_id=ord_id,
        itm_pro_id=pro_id,
        itm_stock=stock
    )


def get_items_by_id_order(id: int) -> list:
    return (orderitems.select(orderitems.itm_stock, product)
        .join(product, on=(orderitems.itm_pro_id==product.pro_id), attr='p')
        .where(orderitems.itm_ord_id == id))

