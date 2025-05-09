from flask import request, jsonify
from flask_restful import Resource
from schemas.user_schema import UserSchema
from models.user import User
from database import db
from services import user_service
from flask_jwt_extended import create_access_token

user_schema = UserSchema()

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        if user_service.get_user_by_username(data['username']):
            return {"message": "User with that username already exists"},