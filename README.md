# BookAPI

BookAPI kullanıcıların kütüphane üzerinde CRUD işlemlerini yapabilmesini sağlar.

**Dependencies:** Python 3.8.0, Pip, Virtualenv

### Create virtual environment 

```sh
git clone https://github.com/mertbilgic/BookAPI.git
cd BookAPI
virtualenv venv
```

### Install depedencies

```sh
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Start

```sh
$ python app.py 
```

##### Hello World
 API ımızı test ederek başlayalım.Terminali açalım ve aşağıdaki komutu girelim.
```sh
# GET /
curl http://127.0.0.1:5000/
This is BookAPI
```
Kütüphanedeki kitapları listelemek için aşağıdaki komutu kullanırız.
```sh
# GET /books
curl http://127.0.0.1:5000/books
{
  "books": [
    {
      "author": "Test", 
      "isbn": 123123321, 
      "name": "Test Book2", 
      "price": 7.99
    }
  ]
}
```
API mızın sonucuna baktığımızda JSON olmasını bekliyoruz.API'nin header'ını almak için **-i** ekleyelim.

```sh
# GET /books
curl -i http://127.0.0.1:5000/books
{
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 133
Server: Werkzeug/1.0.1 Python/3.8.3
Date: Wed, 24 Jun 2020 15:10:12 GMT

  "books": [
    {
      "author": "Test", 
      "isbn": 123123321, 
      "name": "Test Book2", 
      "price": 7.99
    }
  ]
}

```
Beklendiği gibi, Content-Type application/json'dur.

Kütüphanedeki kitapları ISBN numarası ile listelemek için aşağıdaki komutu kullanırız.
```sh
# GET /books<int:isbn>
curl http://127.0.0.1:5000/books/123123321
{
  "books": [
    {
      "author": "Test", 
      "isbn": 123123321, 
      "name": "Test Book2", 
      "price": 7.99
    }
  ]
}
```
BookAPI'daki diğer endpoint'lere request atabilmemiz için token'a ihtiyacımız var.Bunun için BookAPI'a kayıt oluyoruz.Response kodu 204 olduğu için bize herhangi bir içerik dönmez.
```sh
# POST /signup
curl -X POST http://localhost:5000/signup \
-d '{
  "username":"testuser", 
  "password":"123456"
  }' \
-H "Content-Type: application/json" 
```

BookAPI'a login olduğumuzda response olarak bize bir token döner.Bu token'ı diğer requestlerimizde kullacağız.
```sh
# GET /login
curl -X GET http://localhost:5000/login \
-d '{
  "username":"testuser", 
  "password":"123456"
  }' \
-H "Content-Type: application/json" 

Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ5MDIwNjJ9.QQeSUCA6Ox2Ioz73bL1P4NdE2Y8YoZLjanfAN40U6s8  
```

Kütüphaneye yeni bir kitab eklemek için aşadağıdaki komutu kullanabiliriz.
```sh
# POST/books
curl -X POST 'http://127.0.0.1:5000/books?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ5MDgxNzZ9.v9sASWb0WJeDjuad4hWwth8jjpsAe85hh1O09-UyHOs%20%20' \
-H 'Content-Type: application/json' \
-d'{
	"name": "New Add Test Book",
	"price": 9.99,
	"isbn": 987654321,
	"author": "New Test 123"
}'

Result:
{
    "status": "success",
    "data": {
        "author": "New Test 123",
        "name": "New Add Test Book",
        "price": 9.99,
        "isbn": 987654321
    }
}
```
Kütüphanedeki bir kitabı silmek için aşadağıdaki komutu kullanabiliriz.
```sh
# DELETE /books<int:isbn>
curl --location -X DELETE 'http://127.0.0.1:5000/books/987654321?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ5MDgxNzZ9.v9sASWb0WJeDjuad4hWwth8jjpsAe85hh1O09-UyHOs%20%20' \
-H 'Content-Type: application/json' \
```

Kütüphanedeki bir kitabı replace etmek için aşadağıdaki komutu kullanabiliriz.
```sh
# PUT /books<int:isbn>
curl -X PUT 'http://127.0.0.1:5000/books/123123321?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ5MDgxNzZ9.v9sASWb0WJeDjuad4hWwth8jjpsAe85hh1O09-UyHOs%20%20' \ 
-H "Content-Type: application/json" \
-d '{
        "name": "New Test Book",
        "price": 99.99,
        "isbn": 123123321,
        "author": "New Test"
}'
```
Kütüphanedeki bir kitabın değerlerinin bir kısmını replace etmek için aşadağıdaki komutu kullanabiliriz.
```sh
# PATCH /books<int:isbn>
curl -X PATCH 'http://127.0.0.1:5000/books/123123321?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ5MDgxNzZ9.v9sASWb0WJeDjuad4hWwth8jjpsAe85hh1O09-UyHOs%20%20' \
-H 'Content-Type: application/json' \
-d'{
	"name": "New Add Test PATCH"
}'
```