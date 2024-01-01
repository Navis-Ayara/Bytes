from flask import Flask, jsonify, request
from app import db
import uuid
from passlib.hash import pbkdf2_sha256
class User:
    def signup(self):
# user object creation
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "password": request.form.get('password'),
        }
        # encryption
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        user['name'] = pbkdf2_sha256.encrypt(user['name'])

        # write to db
        if db.users.find_one({'name': user['name']}):
            return jsonify({'message': 'User already exists'}), 409
        db.users.insert_one(user)

        if db.users.insert_one(user):
            return jsonify({"message": "Registration Successful"}), 200

        return jsonify({"error": "Registration Failed"}), 400