import numpy as np
import pandas as pd

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def model_lasso(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=None)
    reg = Lasso(alpha=1)
    reg.fit(X_train, y_train)
    Lasso(alpha=1)
    print('R squared training set', round(reg.score(X_train, y_train)*100, 2))
    print('R squared test set', round(reg.score(X_test, y_test)*100, 2))
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