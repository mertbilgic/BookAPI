from flask import Flask, jsonify, request, Response
from helpers import response_helpers as rp
from helpers import data_cleaner_helpers as cl
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

books = [
    {
        'name': 'Veri Yapıları ve Algoritmalar',
        'price': 65,
        'author': 'Rıfat Çölkesen',
        'isbn': 987654321
    },
    {
        'name': 'Steve Jobs',
        'price': 50,
        'author': 'Walter Isaacson',
        'isbn': 123456789
    }
]

@app.route('/books')
def get_books():
    return jsonify({'books':books})

@app.route('/books',methods=['POST'])
def add_book():
    request_data = request.get_json()
    response_data,valid = rp.craate_response(request_data)
    response = ""

    if valid:
        response = Response(json.dumps(response_data),status=201,mimetype='applicaton/json')
        new_book = cl.data_cleaner(request_data)
        response.headers['Location'] = '/books/' + str(new_book['isbn'])
        books.insert(0, new_book)
    else :
        response = Response(json.dumps(response_data),status=400,mimetype='applicaton/json')
        
    return response

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'author': book['author'],
                'name': book['name'],
                'price': book['price'],
                "isbn": book["isbn"]
            }
    return jsonify(return_value)

if __name__ == '__main__':
    app.run(debug=True)