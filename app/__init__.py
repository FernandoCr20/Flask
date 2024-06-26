from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'

db = SQLAlchemy(app)
from app.models.products import Products
with app.app_context():
    db.create_all()

from app.view.reso_products import Index
from app.view.reso_products import ProductById
from app.view.reso_products import ProductCreate
from app.view.reso_products import ProductUpdate
from app.view.reso_products import ProductDelete

api.add_resource(Index, '/')
api.add_resource(ProductById, '/buscar_id') #get
api.add_resource(ProductCreate, '/criar') # post
api.add_resource(ProductUpdate, '/atualizar') # put
api.add_resource(ProductDelete, '/deletar') # delete

''' @app.route("/")
def index():
    # return "<h1> Minha aplicacao em flask </h1>"
    return render_template("index.html") '''