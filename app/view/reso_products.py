from flask_restful import Resource, reqparse
from app.models.products import Products
from flask import jsonify

class Index(Resource):
    def get(self):
        return jsonify("Welcome to my aplication flask")

class ProductCreate(Resource):
    def post(self):
        try:
            return {"message": 'Products create successfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500