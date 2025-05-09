from flask import jsonify
from flask_restful import Resource
from schemas.product_schema import ProductSchema
from models.product import Product
from database import db

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)