# non viene usata visto che i dati interni non sono ottimali!

import numpy as np
import pandas as pd

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def model_lasso(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=None)
    reg = Lasso(alpha=1)
    reg.fit(X_train, y_train)
    Lasso(alpha=1)
    # train data
    pred_train = reg.predict(X_train)
    mse_train = mean_squared_error(y_train, pred_train)
    print('MSE training set', round(mse_train, 2))
    # Test data
    pred = reg.predict(X_test)
    mse_test =mean_squared_error(y_test, pred)
    print('MSE test set', round(mse_test, 2))
    p = reg.predict(X_test)
    return mean_squared_error(y_test, p)

def model_lasso_v2(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=None)
    model_lasso = Lasso(alpha=0.01)
    model_lasso.fit(X_train, y_train) 
    pred_train_lasso= model_lasso.predict(X_train)
    print(np.sqrt(mean_squared_error(y_train,pred_train_lasso)))
    print(r2_score(y_train, pred_train_lasso))
    pred_test_lasso= model_lasso.predict(X_test)
    print(np.sqrt(mean_squared_error(y_test,pred_test_lasso))) 
    print(r2_score(y_test, pred_test_lasso))
    