from models.user import User
from database import db

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()