import json

def get_error_data(filepath):
    data = json.load(open(filepath))
    max_error = 0
    min_error = value[0]['error']
    for value in data:
        if value['error']> max_error:
            max_error = value['error']
        if value['error']> min_err:
            max_error = value['error']