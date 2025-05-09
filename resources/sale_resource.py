from flask import request, jsonify
from flask_restful import Resource
from schemas.sale_schema import SaleSchema
from services import sale_service
from flask_jwt_extended import jwt_required, get_jwt_identity

sale_schema = SaleSchema()

class RecordSaleResource(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        errors = sale_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        sale, error_message = sale_service.record_sale(
            data['store_id'], data['product_id'], data['quantity']
        )

        if sale:
            return sale_schema.dump(sale), 201
        else:
            return {"message": error_message}, 400