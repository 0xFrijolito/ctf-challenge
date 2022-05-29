from App import app, db
from App.models.users import Users
from App.helpers import jwt

from functools import wraps
from flask import request, jsonify

def is_login (f):
    @wraps(f)
    def decorator(*args, **kws):
        session_cookie = request.cookies.get("session")
        if not session_cookie:
            return jsonify({"message": "session cookie is missing"}), 401

        try:
            data = jwt.decode(session_cookie)
            user = Users.query.get(data.get("id"))
        except:
            return jsonify({"message": "not valid session cookie"}), 401

        return f(user, *args, **kws)      
    return decorator