
def validBookObject(bookObject):
    keys = {"author", "name",  "price", "isbn"}
    nothing_keys = []
    for key in keys:
        if key not in bookObject:
            nothing_keys.append(key)
    
    return nothing_keys
