import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from file_opening import datas


def regress(filepath):
    X = np.array([datas(filepath).Open, datas(filepath).Low, datas(filepath).High])
    X = X.transpose()
    y = datas(filepath).Close
    '''  
    print(X.shape)
    print(y.shape)
    '''
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=None)
    model = LinearRegression()
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    m = mean_absolute_error(y_test,p)
    '''    
    plt.figure()
    plt.plot(datas(filepath)["Date"], p, color = 'r')
    plt.plot(datas(filepath)["Date"].iloc[:y_test.shape[0]:], y_test, alpha = .2)
    plt.plot(y)
    plt.show()
    '''
    return m
