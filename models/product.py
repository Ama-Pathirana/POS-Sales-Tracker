from database import db

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    stock_quantity = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    sale_items = db.relationship('SaleItem', backref='product', lazy=True)

    def __repr__(self):
        return f"<Product {self.product_name}>"