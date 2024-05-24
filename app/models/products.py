from app import db

class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def list_id(self, product_id):
        try:
            products = db.session.query(Products).filter(Products.id == product_id).all()
            products_dict = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products] 
            return products_dict
        except Exception as e:
            print("error ao buscar lista de produtos", e)


    def save_products(self, name, price):
        try:
            add_banco = Products(name, price)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print("Erro ao salvar produtos", e)

    def update_products(self, id, name, price):
        try:
            db.session.query(Products).filter(Products.id == id).update({"name":name, "price":price})
            db.session.commit()
        except Exception as e:
            print("Erro ao salvar produtos", e)

    def delete_products(self, id):
        try:
            db.session.query(Products).filter(Products.id == id).delete()
            db.session.commit()
        except Exception as e:
            print("Erro ao deletar o produto", e)