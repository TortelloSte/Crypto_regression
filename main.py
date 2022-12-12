from utilities.file_operation import read_files, write_errors_file

if __name__ == '__main__':
    filepath = 'C:/Users/StefanoPerdicchia/Crypto_regression/archive'
    output_error_path = "C:/Users/StefanoPerdicchia/Crypto_regression/error.json"
    test = read_files(filepath, output_error_path)

    # plt.plot(p, color = 'r')
    # plt.plot(X_test, alpha = .2)
    # plt.show()