from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from file_opening import datas


def modello_rete(filepath):
    model = Sequential()
    model.add(Dense(datas(filepath).shape[1]-1, activation= 'relu'))
    model.add(Dense(20, activation= "relu"))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(1, activation='relu'))
    model.compile(optimizer = Adam(learning_rate = 0.01), loss='mean_squared_error')
    
    y = datas(filepath)["Close"]
    x = datas(filepath).drop(["Close", 'Date_year','Date_month','Date_day'], axis= 1)
    x_train, x_test, y_train, y_test= train_test_split(x, y, shuffle=True, test_size = 0.1)
    model.fit(x_train, y_train, epochs= 50, batch_size= 32)
    pred= model.predict(x_test)
    mse= mean_squared_error(y_test, pred)
    return mse
    #print(model.summary())