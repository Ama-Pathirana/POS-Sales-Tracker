from flask import Flask
from flask_restful import Api
from database import db, init_db, app as flask_app
from resources.product_resource import ProductResource, ProductListResource
from resources.store_resource import StoreResource, StoreListResource
from resources.sale_resource import RecordSaleResource
from resources.inventory_resource import InventoryStatusResource
from resources.summary_resource import HourlySalesSummaryResource
from resources.auth_resource import RegisterResource, LoginResource
from tasks.scheduler import start_scheduler
from flask_jwt_extended import JWTManager
from utils import roles_required
from models.sale_item import SaleItem # Import the new model

api = Api(flask_app)

# Add resources to the API
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(ProductListResource, '/products')
api.add_resource(StoreResource, '/stores/<int:store_id>')
api.add_resource(StoreListResource, '/stores')
api.add_resource(RecordSaleResource, '/sales')
api.add_resource(InventoryStatusResource, '/inventory/<int:product_id>')
api.add_resource(HourlySalesSummaryResource, '/stores/<int:store_id>/summaries')
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')

# Setup JWT
flask_app.config["JWT_SECRET_KEY"] = flask_app.config.get('SECRET_KEY')
jwt = JWTManager(flask_app)

@jwt.user_identity_loader
def user_identity_lookup(identity):
    from services import user_service
    user = user_service.get_user_by_username(identity)
    if user:
        return user.user_id
    return None

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    from services import user_service
    user = user_service.get_user_by_username(identity)
    if user:
        return {'role': user.role}
    return {}

if __name__ == '__main__':
    # You might not need to initialize the DB here if it's already created in MySQL
    # init_db()
    start_scheduler()
    flask_app.run(debug=True)
