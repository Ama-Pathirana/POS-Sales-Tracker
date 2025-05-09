from marshmallow import Schema, fields

class ProductSchema(Schema):
    product_id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True)
    price = fields.Decimal(required=True)
    stock_quantity = fields.Int(required=True)
    store_id = fields.Int() # You might not want to expose this for creation/update