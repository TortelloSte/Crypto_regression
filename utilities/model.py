import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

def create_model(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=None)
    model = LinearRegression()
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(np.arange(stop=p.shape[0]), p, color='r', alpha=.9, marker='.')
    ax2.plot(np.arange(stop=y_test.shape[0]), y_test, color='b', alpha=.9, marker='.')
    plt.show()
    return mean_squared_error(y_test, p)
    #return mean_absolute_error(y_test,p)
