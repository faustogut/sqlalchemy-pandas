#https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/

import db
from models import Producto
def run():
    arroz = Producto('Arroz', 1.25)
    db.session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3)
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)

    print("----")
    productos = db.session.query(Producto).all()
    print(productos)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()

