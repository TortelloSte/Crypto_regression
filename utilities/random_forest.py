import numpy as np 
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def random_forest_V1(df):
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=None)
    rf = RandomForestRegressor(n_estimators = 300, random_state = 42)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    errors = abs(predictions - y_test) # da cambiare
    # print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / y_test)
    accuracy = 100 - np.mean(mape)
    # lo salva come lista va cambiata la cosa!!!

    return (accuracy, 2)
