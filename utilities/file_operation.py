import glob
import pandas as pd
import json
from utilities.model import create_model
#from utilities.model_lasso import model_lasso
from sklearn.preprocessing import StandardScaler 


def read_files(filepath, error_file_path):
    errors = []
    filenames = []
    for filename in glob.glob(f'{filepath}/*.csv'):
        filenames.append(filename)
        df = pd.read_csv(filename, sep=',', header=0)
        df.drop('SNo', axis = 1, inplace=True)
        df.columns = df.columns.str.lower()
        #errors.append(create_model(df))
        errors.append(create_model(df))
    write_errors_file(error_file_path, errors, filenames)
    pass


def write_errors_file(error_file_path, errors, filenames):
    result = []
    for filename, error in zip(filenames, errors):
        result.append({'file': filename, 'error': error})
    json.dump(result, open(error_file_path, "w"), indent=4)
    pass



if __name__ == '__main__':
    filepath = 'C:/Users/StefanoPerdicchia/Crypto_regression/archive'
    output_error_path = ""
    test = read_files(filepath)