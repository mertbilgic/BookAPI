from helpers.validation_helpers import *
from helpers.data_cleaner_helpers import *

def craate_response(request_data):

    nothing_keys = validBookObject(request_data)
    response = {}
    valid = True

    if nothing_keys:
        message = "Invalid book object missing key in request"
        error_type = "KeyError"
        code = 2101
        response = create_error_response(nothing_keys,message,error_type,code)
        valid = False
    else:
        response = create_succes_response(request_data)
    
    return response,valid

def create_error_response(nothing_keys,message,error_type,code):

    response = { 
        "error": {
            "message": message,
            "missingKey":" ".join(nothing_keys),
            "type": error_type,
            "code": code,
            "helper": "Data passed in similar to this {'name':'bookname','author':'xxxx','price':'7.99','isbn':'1231231231231'}"
        }
    }
    return response
        
def create_succes_response(request_data):
    response = {
        "status" : "success",
        "data" : data_cleaner(request_data),
    }
    return response