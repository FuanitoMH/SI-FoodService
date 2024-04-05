from peewee import *


# Instancia de la base de datos
db = MySQLDatabase('foodservice', user='root', passwd='pass', host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = db

