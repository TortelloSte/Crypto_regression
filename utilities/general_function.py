import json

def get_error_data(filepath):
    data = json.load(open(filepath))
    max_error = 0
    max_label = ""
    min_error = data[0]['error']
    min_label = data[0]['file']

    for value in data:
        if value['error'] > max_error: # da errore quando entra in questo if, da cambiare da lista a int (da errore il maggiore!!!)
            max_error = value['error']
            max_label = value['file']
        if value['error'] < min_error:
            min_error = value['error']
            min_label = value['file']
    return  min_error, min_label, max_error, max_label


if __name__ == '__main__':
    print(get_error_data("./error.json"))