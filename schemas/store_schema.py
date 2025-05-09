from marshmallow import Schema, fields

class StoreSchema(Schema):
    store_id = fields.Int(dump_only=True)
    store_name = fields.Str(required=True)
    location = fields.Str()