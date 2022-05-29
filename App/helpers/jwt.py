import jwt

from App import app

def encode (data):
    return jwt.encode(data, app.config["SECRET_KEY"], algorithm="HS256")

def decode (data):
    return jwt.decode(data, app.config["SECRET_KEY"], algorithms=["HS256"])