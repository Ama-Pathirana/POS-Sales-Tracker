from flask import jsonify
from flask_restful import Resource
from schemas.product_schema import ProductSchema
from models.product import Product
from flask_jwt_extended import jwt_required

product_schema = ProductSchema()

class InventoryStatusResource(Resource):
    @jwt_required()
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return {"product_name": product.product_name, "current_stock": product.stock_quantity}