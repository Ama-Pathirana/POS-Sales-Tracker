from models.product import Product
from database import db

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def update_product_stock(product_id, quantity): # You might not need this standalone now
    product = get_product_by_id(product_id)
    if product:
        product.stock_quantity -= quantity
        db.session.commit()
        return True
    return False