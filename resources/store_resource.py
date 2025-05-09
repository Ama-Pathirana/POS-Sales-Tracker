from flask import jsonify
from flask_restful import Resource
from schemas.store_schema import StoreSchema
from models.store import Store
from database import db

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

class StoreResource(Resource):
    def get(self, store_id):
        store = Store.query.get_or_404(store_id)
        return store_schema.dump(store)

class StoreListResource(Resource):
    def get(self):
        stores = Store.query.all()
        return stores_schema.dump(stores)