from marshmallow import Schema, fields, List, Nested

class SaleItemInputSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class SaleSchema(Schema):
    sale_id = fields.Int(dump_only=True)
    store_id = fields.Int(required=True)
    sale_date = fields.DateTime(dump_only=True)
    total_amount = fields.Decimal(dump_only=True) # Might calculate this on the fly
    items = List(Nested(SaleItemInputSchema), required=True)