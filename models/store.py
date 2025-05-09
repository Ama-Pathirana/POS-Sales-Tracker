from database import db

class Store(db.Model):
    __tablename__ = 'stores'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100))
    location = db.Column(db.String(255))
    products = db.relationship('Product', backref='store', lazy=True)
    sales = db.relationship('Sale', backref='store', lazy=True)
    summaries = db.relationship('HourlySalesSummary', backref='store', lazy=True) # You'll need to create this model

    def __repr__(self):
        return f"<Store {self.store_name}>"