from database import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'
    sale_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Numeric(10, 2)) # You might not need this if you calculate it

    sale_items = db.relationship('SaleItem', backref='sale', lazy=True)

    def __repr__(self):
        return f"<Sale {self.sale_id}>"