from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    print("Database tables created!")