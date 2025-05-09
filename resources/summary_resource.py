from flask import jsonify
from flask_restful import Resource
from schemas.sales_summary_schema import HourlySalesSummarySchema
from services import summary_service
from flask_jwt_extended import jwt_required
from app import roles_required  # Import the decorator

summary_schema = HourlySalesSummarySchema(many=True)

class HourlySalesSummaryResource(Resource):
    @jwt_required()
    @roles_required(['sales_manager', 'head_office_manager'])
    def get(self, store_id):
        summaries = summary_service.get_hourly_summaries_by_store(store_id)
        return summary_schema.dump(summaries)
