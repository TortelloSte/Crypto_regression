import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def create_model(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    # print(X.shape)
    # print(y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, shuffle=None)
    model = LinearRegression()
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    return mean_absolute_error(y_test,p)




# dopo provo a vedere di sistemare la regressione e non usare sklearn ma farla in scratch
# k, 


#     fileoutputname = 'C:/Users/StefanoPerdicchia/Crypto_regression/output.txt'

# print(errors)

# with open(fileoutputname, 'w') as f:
#     outputstring = ""
#     for i, error in enumerate(errors):
#         outputstring += f'file {i + 1}, errore: {error}\n'
#     f.write(outputstring)

    # questo deve uscire in output della funzione
    