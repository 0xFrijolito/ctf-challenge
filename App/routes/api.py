import decimal
import hashlib

from App import app, db
from App.models.users import Users
from App.models.transactions import Transaction
from App.helpers import jwt, auth

from flask import jsonify, request

def response(data):
    return jsonify({"message": data})

@app.route("/api/login", methods=["POST"])
def login_api ():
    req = request.json
    if not req.get("email") or not req.get("password"):
        return response("invalid request"), 400

    user = Users.query.filter_by(email = req.get("email")).first()
    if not user:
        return response("invalid credentials"), 401

    if user.password != req.get("password"):
        return response("invalid credentials"), 401

    jwt_payload = {"id": user.id, "username": user.username, "wallet": user.wallet, "balance": str(user.coins)}
    jwt_token   = jwt.encode(jwt_payload)

    return response({"jwt": jwt_token, "data": jwt_payload}), 200


@app.route("/api/register", methods=["POST"])
def registe_api ():
    req = request.json
    if not req.get("username") or not req.get("email") or not req.get("password"):
        return response("invalid request"), 400

    if Users.query.filter_by(email=req.get("email")).first():
        return response("There is already a user with that email"), 400
        
    if Users.query.filter_by(username=req.get("username")).first():
        return response("There is already a user with that username"), 400
    
    new_user = Users(
        username = req.get("username"),
        email = req.get("email"),
        password = req.get("password"),
        wallet = hashlib.md5(req.get("username").encode()).hexdigest(),
        coins = 0.1
    )

    db.session.add(new_user)
    db.session.commit()

    return response("user created successfully"), 200

@app.route("/api/get_user", methods=["GET"])
@auth.is_login
def get_transaction_api (user):
    return response({"user": user.as_dict()})

@app.route("/api/get_transactions", methods=["GET"])
@auth.is_login
def get_user_api (user):
    transactions = Transaction.query.filter((Transaction.sender==user.wallet) | (Transaction.reciver==user.wallet) ).all()
    return response({"transactions": [t.as_dict() for t in transactions]})

@app.route("/api/create_transaction", methods=["POST"])
@auth.is_login
def create_transaction_api (user):
    req = request.json
    if not req.get("to") or not req.get("amount"):
        return response("Invalid request"), 400

    # Validation 
    reciver = Users.query.filter_by(wallet=req.get("to")).first()
    if not reciver: return response("There is no user with that wallet"), 400
    if float(req.get("amount")) > user.coins: return response("Insufficient balance"), 400
    if req.get("to") == user.wallet: return response("You can't send yourself coins"), 400

    # Create the transaction
    new_transaction = Transaction(sender = user.wallet, reciver = req.get("to"), amount = req.get("amount"))
    
    # Update users balance 🤔
    user.coins -= decimal.Decimal(float(req.get("amount")))
    reciver.coins += decimal.Decimal(float(req.get("amount")))

    db.session.add(new_transaction)
    db.session.commit()

    return response("transaction create succefuly")
