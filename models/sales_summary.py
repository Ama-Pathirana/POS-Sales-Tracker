from database import db
from datetime import datetime

class HourlySalesSummary(db.Model):
    summary_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=False)
    summary_datetime = db.Column(db.DateTime, nullable=False)
    total_sales = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<HourlySalesSummary for Store {self.store_id} at {self.summary_datetime}>"