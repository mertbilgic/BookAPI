from flask import Flask, jsonify

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

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'author': book['author'],
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)

if __name__ == '__main__':
    app.run(debug=True)