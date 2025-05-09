from database import db

class SaleItem(db.Model):
    __tablename__ = 'sale_items'
    sale_item_id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.sale_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer)
    item_price = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f"<SaleItem {self.sale_item_id}>"