from flask import Flask, jsonify, request, Response
from helpers import response_helpers as rp
from helpers import data_cleaner_helpers as cl
from model.book_model import Book
from settings import *
import json


@app.route('/')
def index():
    return "This is BookAPI"

@app.route('/books')
def get_books():
    return jsonify({'books': Book.get_all_book()})

@app.route('/books',methods=['POST'])
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

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = Book.get_book_json(isbn)
    return jsonify(return_value)

@app.route('/books/<int:isbn>', methods=['PUT'])
def update_book_all_elements(isbn):
    request_data = request.get_json()
    response_data,valid = rp.craate_response(request_data)
    
    if not valid:
        response = Response(json.dump(response_data),status=400,mimetype='applicaton/json')
        return response
    
    Book.update_book(isbn, request_data['name'], request_data['price'], request_data['author'])
    response = Response("",status=204)
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
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

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):

    if(Book.delete_book(isbn)):
        response = Response("",status=204)
        return response

    message = {'error':'ISBN number not found'}
    response = Response(json.dumps(message),status=404,mimetype='applicaton/json')
    return response

if __name__ == '__main__':
    app.run(debug=True)