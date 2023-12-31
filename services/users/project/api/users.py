from flask import Blueprint, jsonify, request
from project import db
from project.api.models import User
from sqlalchemy import exc

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/ping")
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route("/users", methods=["POST"])
def add_user():
    post_data = request.get_json()
    response_object = {
        "status": "fail",
        "message": "Invalid payload."
    }
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get("username")
    email = post_data.get("email")
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object['message'] = 'success'
            response_object["status"] = f"{email} was added!"
            return jsonify(response_object), 200
        else:
            response_object["message"] = 'Sorry! That email already exists.'
            return jsonify(response_object), 400
    except exc.IntegrityError as exe:
        db.session.rollback()
        return jsonify(response_object), 400

