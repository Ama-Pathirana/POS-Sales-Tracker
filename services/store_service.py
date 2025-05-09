from models.store import Store
from database import db

def get_store_by_id(store_id):
    return Store.query.get(store_id)