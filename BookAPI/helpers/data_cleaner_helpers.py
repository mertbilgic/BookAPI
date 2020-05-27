def data_cleaner(request_data):
    new_book = {
        "author": request_data["author"],
        "name": request_data["name"],
        "price": request_data["price"],
        "isbn": request_data["isbn"]
    }
    return new_book