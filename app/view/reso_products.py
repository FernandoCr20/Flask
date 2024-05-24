from flask_restful import Resource, reqparse
from app.models.products import Products
from flask import jsonify

argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)

argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos_update.add_argument('price', type=float)

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

args = reqparse.RequestParser()
args.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome to my aplication flask")

class ProductById(Resource):
    def get(self):
        try:
            datas = args.parse_args()
            print(datas)
            products = Products.list_id(self, datas['id'])
            if products:
                return products
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Products.save_products(self, datas['name'], datas['price'])
            return {"message": 'Products create succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            print(datas)
            Products.update_products(self, datas['id'], datas['name'], datas['price'])
            return {"message": 'Products update succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class ProductDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            print(datas)
            Products.delete_products(self, datas['id'])
            return {"message": 'Products deleted'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500