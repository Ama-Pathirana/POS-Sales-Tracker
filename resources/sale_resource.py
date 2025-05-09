from flask import request, jsonify
from flask_restful import Resource
from schemas.sale_schema import SaleSchema
from services import sale_service
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import roles_required  # Import the decorator

sale_schema = SaleSchema()

class RecordSaleResource(Resource):
    @jwt_required()
    @roles_required(['cashier', 'sales_manager'])
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        try:
            sale_data = sale_schema.load(data)
        except Exception as e:
            return {"errors": str(e)}, 400

        sale, error_message = sale_service.record_sale(
            sale_data['store_id'], sale_data['items']
        )

        if sale:
            return {"message": "Sale recorded successfully", "sale_id": sale.sale_id}, 201
        else:
            return {"message": error_message}, 400
