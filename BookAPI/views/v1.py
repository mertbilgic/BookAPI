
import json
import datetime

from flask import Flask, jsonify, request, Response,Blueprint
import jwt

from bookapi.helpers import response_helpers as rp
from bookapi.helpers import data_cleaner_helpers as cl
from bookapi.dbmodel.book_model import Book
from bookapi.dbmodel.user_model import User
from bookapi import app,SECRET_KEY,DEFAULT_PAGE_LIMIT
from bookapi.helpers.token_helper import *


api_v1 = Blueprint('api_v1', __name__, url_prefix="/api/v1")

@api_v1.route('/login')
def get_token():
    request_data = request.get_json()
    try:
        username = request_data['username']
        password = request_data['password']
    except TypeError:
        return jsonify({"helper": "Data passed in similar to this {'username':'test','password':'password'}"})
    
    match = User.username_password_match(username, password)
    if match:
        expretaion_date = datetime.datetime.now() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expretaion_date}, SECRET_KEY, algorithm='HS256')
        return token
    else:
        return Response('',401,mimetype='application/json')

@api_v1.route('/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    try:
        username = request_data['username']
        password = request_data['password']
    except ValueError:
        return jsonify({"helper": "Data passed in similar to this {'username':'test','password':'password'}"})
    User.create_user(username, password)

    response = Response("",status=204)
    return response

@api_v1.route('/books')
def get_books():
    return jsonify({'books': Book.get_all_book()})

@api_v1.route('/books',methods=['POST'])
@token_required
def add_book():
    request_data = request.get_json()
    response_data,valid = rp.craate_response(request_data)
    if valid:
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'], request_data['author'])
        response = Response(json.dumps(response_data),status=201,mimetype='applicaton/json')
        response.headers['Location'] = '/books/' + str(request_data['isbn'])
        return response
    else :
        response = Response(json.dumps(response_data),status=400,mimetype='applicaton/json')
        return response

@api_v1.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = Book.get_book_json(isbn)
    return jsonify(return_value)

@api_v1.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def update_book_all_elements(isbn):
    request_data = request.get_json()
    response_data,valid = rp.craate_response(request_data)
    
    if not valid:
        response = Response(json.dump(response_data),status=400,mimetype='applicaton/json')
        return response
    
    Book.update_book(isbn, request_data['name'], request_data['price'], request_data['author'])
    response = Response("",status=204)
    return response

@api_v1.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def update_book(isbn):
    request_data = request.get_json()
    book_data = Book.get_book_json(isbn)

    for k,v in request_data.items():
        if bool(book_data.get(k)):
            book_data[k] = v
    
    Book.update_book(isbn, book_data['name'], book_data['price'], book_data['author'])
    response = Response("",status=204)
    response.headers['Location'] = '/books/' + str(isbn)

    return response

@api_v1.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):

    if(Book.delete_book(isbn)):
        response = Response("",status=204)
        return response

    message = {'error':'ISBN number not found'}
    response = Response(json.dumps(message),status=404,mimetype='applicaton/json')
    return response