# Importa le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense

# il codice sviluppato precedentemente prendeva in input dei csv che ora non si possiedono quindi sono andato a posteriori a modificare il codice per renderlo funzionante


def train_and_predict_lstm(csv_file):
    # Leggi il dataset completo da un file CSV
    dataset = pd.read_csv(csv_file)
    dataset = dataset[['Open']]  # Assicurati di selezionare la colonna corretta

    # Dividi il dataset in set di addestramento e test (ad esempio, 80% - 20%)
    train_size = int(len(dataset) * 0.8)
    train_set = dataset[:train_size].values
    test_set = dataset[train_size:].values

    # Esegui la normalizzazione dei dati tra 0 e 1
    sc = MinMaxScaler(feature_range=(0,1))
    train_set_scaled = sc.fit_transform(train_set)
    test_set_scaled = sc.transform(test_set)

    # Prepara i dati di addestramento per il modello LSTM
    X_train, y_train = [], []
    for i in range(60, len(train_set_scaled)):
        X_train.append(train_set_scaled[i-60:i, 0])
        y_train.append(train_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    # Crea un modello sequenziale LSTM
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # Compila il modello LSTM
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Addestra il modello con i dati di addestramento
    model.fit(X_train, y_train, epochs=100, batch_size=32)

    # Prepara i dati di test per il modello LSTM
    X_test, y_test = [], []
    for i in range(60, len(test_set_scaled)):
        X_test.append(test_set_scaled[i-60:i, 0])
        y_test.append(test_set_scaled[i, 0])
    X_test, y_test = np.array(X_test), np.array(y_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Effettua previsioni con il modello LSTM
    predicted_stock_price = model.predict(X_test)

    # Reverti la normalizzazione per ottenere i prezzi previsti iniziali
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    # Visualizza i risultati
    plt.plot(test_set, color='black', label='Prezzo in stock')
    plt.plot(predicted_stock_price, color='green', label='Dati predetti')
    plt.title('LSTM Analisi')
    plt.xlabel('Tempo')
    plt.ylabel('TATA Stock Price')
    plt.legend()
    plt.show()

    return model, predicted_stock_price


trained_model, predictions = train_and_predict_lstm('./DATA/archive/coin_Bitcoin.csv')

'''
# Leggi il dataset di addestramento da un file CSV
dataset_train = pd.read_csv('dataset_train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Esegui la normalizzazione dei dati tra 0 e 1
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

# Prepara i dati di addestramento per il modello LSTM
X_train = []
y_train = []
for i in range(60, 2035):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Crea un modello sequenziale LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compila il modello LSTM
model.compile(optimizer='adam', loss='mean_squared_error')

# Addestra il modello con i dati di addestramento
model.fit(X_train, y_train, epochs=100, batch_size=32)

# Leggi il dataset di test da un file CSV
dataset_test = pd.read_csv('dataset_test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# Concatena il dataset di addestramento e di test per preparare i dati di input
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis=0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

# Prepara i dati di test per il modello LSTM
X_test = []
for i in range(60, 76):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Effettua previsioni con il modello LSTM
predicted_stock_price = model.predict(X_test)

# Reverti la normalizzazione per ottenere i prezzi previsti iniziali
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualizza i risultati
plt.plot(real_stock_price, color='black', label='Prezzo in stock')
plt.plot(predicted_stock_price, color='green', label='Dati predetti')
plt.title('LSTM Analisi')
plt.xlabel('Tempo')
plt.ylabel('TATA Stock Price')
plt.legend()
plt.show()
'''