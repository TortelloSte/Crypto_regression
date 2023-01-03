import glob
import pandas as pd


def read_files(filepath):
    filenames = []
    for filename in glob.glob(f'{filepath}/*.csv'):
        filenames.append(filename)
        df = pd.read_csv(filename, sep=',', header=0)
        df.drop('SNo', axis = 1, inplace=True)
        df.columns = df.columns.str.lower()


if __name__ == '__main__':
    filepath = '../Crypto_regression/archive'
    test = read_files(filepath)