from bookapi import app
from functools import wraps,update_wrapper
from flask import request,jsonify
from jwt import decode

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            decode(token,app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({"error": "Need a valid token to view this page"})
    return wrapper
    

