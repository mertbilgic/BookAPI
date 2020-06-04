import json
from flask import Flask
from settings import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

"""
    Create db model

    $python3
    >>> from model.book_model import db
    >>> db.create_all()
    >>> exit()

"""
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(80))

    def convert_json(self):
        return {'name': self.name, 'price': self.price, 'isbn': self.isbn, 'author': self.author}

    def add_book(_name, _price, _isbn, _author):
        new_book = Book(name=_name, price=_price, isbn=_isbn, author=_author)
        db.session.add(new_book)
        db.session.commit()

    def get_all_book():
        return [Book.convert_json(book) for book in Book.query.all()]
    
    def get_book_json(_isbn):
        return Book.convert_json(Book.query.filter_by(isbn=_isbn).first())
    
    def get_book(_isbn):
        return Book.query.filter_by(isbn=_isbn).first()
    
    def delete_book(_isbn):
        is_successful = Book.query.filter_by(isbn=_isbn).delete()
        db.session.commit()
        return bool(is_successful)

    def update_book_price(_isbn, _price):
        book = Book.get_book(_isbn)
        book.price = _price
        db.session.commit()

    def update_book_name(_isbn, _name):
        book = Book.get_book(_isbn)
        book.name = _name
        db.session.commit()  
    
    def update_book_name(_isbn, _author):
        book = Book.get_book(_isbn)
        book.author = _author
        db.session.commit()   

    def update_book(_isbn, _name, _price, _author):
        book = Book.get_book(_isbn)
        book.name = _name
        book.price = _price
        book.author = _author
        db.session.commit()  

    def __repr__(self):
        book_object = {
            'name':self.name,
            'price':self.price,
            'isbn':self.isbn,
            'author':self.author
        }
        return json.dumps(book_object)

