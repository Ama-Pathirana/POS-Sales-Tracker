from models.sales_summary import HourlySalesSummary
from database import db
from datetime import datetime
from services import sale_service, store_service

def generate_hourly_summary(store_id, dt):
    sales = sale_service.get_sales_by_hour(store_id, dt)
    total_sales = sum(sale.product.price * sale.quantity for sale in sales)
    summary = HourlySalesSummary(store_id=store_id, summary_datetime=dt, total_sales=total_sales)
    db.session.add(summary)
    db.session.commit()
    return summary

def get_hourly_summaries_by_store(store_id):
    return HourlySalesSummary.query.filter_by(store_id=store_id).all()