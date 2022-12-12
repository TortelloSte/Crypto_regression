from utilities.file_operation import read_files
from utilities.general_function import get_error_data

if __name__ == '__main__':
    filepath = '../Crypto_regression/archive'
    output_error_path = "../Crypto_regression/error.json"
    test = read_files(filepath, output_error_path)
    print(get_error_data(output_error_path))