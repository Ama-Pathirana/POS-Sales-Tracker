from marshmallow import Schema, fields

class HourlySalesSummarySchema(Schema):
    summary_id = fields.Int(dump_only=True)
    store_id = fields.Int(required=True)
    summary_datetime = fields.DateTime(required=True)
    total_sales = fields.Float(required=True)