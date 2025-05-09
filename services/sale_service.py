from models.sale import Sale
from models.sale_item import SaleItem
from database import db
from datetime import datetime
from services import product_service, store_service

def record_sale(store_id, items):
    store = store_service.get_store_by_id(store_id)
    if not store:
        return None, "Invalid store ID"

    sale = Sale(store_id=store_id, sale_date=datetime.utcnow(), total_amount=0) # Initialize total
    db.session.add(sale)
    db.session.flush() # To get the sale_id immediately

    total_sale_amount = 0
    for item_data in items:
        product = product_service.get_product_by_id(item_data['product_id'])
        quantity = item_data['quantity']

        if not product:
            db.session.rollback()
            return None, f"Invalid product ID: {item_data['product_id']}"

        if product.stock_quantity < quantity:
            db.session.rollback()
            return None, f"Insufficient stock for {product.product_name}"

        sale_item = SaleItem(
            sale_id=sale.sale_id,
            product_id=product.product_id,
            quantity=quantity,
            item_price=product.price
        )
        db.session.add(sale_item)
        product.stock_quantity -= quantity
        total_sale_amount += product.price * quantity

    sale.total_amount = total_sale_amount
    db.session.commit()
    return sale, None

def get_sales_by_hour(store_id, dt):
    start_of_hour = dt.replace(minute=0, second=0, microsecond=0)
    end_of_hour = start_of_hour.replace(hour=start_of_hour.hour + 1)
    return Sale.query.filter(
        Sale.store_id == store_id,
        Sale.sale_date >= start_of_hour,
        Sale.sale_date < end_of_hour
    ).all()