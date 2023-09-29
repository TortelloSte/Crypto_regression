# Importa le librerie necessarie
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from file_opening import datas

# Definisci una funzione 'modello_rete' che accetta un percorso del file come argomento
def modello_rete_neurale(filepath):
    # Crea un modello sequenziale
    model = Sequential()
    
    # Aggiungi un layer densamente connesso con attivazione ReLU, input_shape basato sul numero di colonne dei dati
    model.add(Dense(datas(filepath).shape[1] - 1, activation='relu'))
    
    # Aggiungi due layer densamente connessi con attivazione ReLU
    model.add(Dense(20, activation='relu'))
    model.add(Dense(20, activation='relu'))
    
    # Aggiungi un layer densamente connesso con attivazione ReLU per l'output
    model.add(Dense(1, activation='relu'))
    
    # Compila il modello specificando l'ottimizzatore (Adam) e la funzione di costo (mean_squared_error)
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mean_squared_error')
    
    # Estrai il target (Close) dai dati utilizzando la funzione 'datas'
    y = datas(filepath)["Close"]
    
    # Estrai le caratteristiche (features) dal DataFrame e rimuovi alcune colonne non necessarie
    x = datas(filepath).drop(["Close", 'Date_year', 'Date_month', 'Date_day'], axis=1)
    
    # Dividi i dati in un set di addestramento (train) e un set di test
    x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.1)
    
    # Addestra il modello con i dati di addestramento per un numero specifico di epoche e batch_size
    model.fit(x_train, y_train, epochs=50, batch_size=32)
    
    # Effettua previsioni sui dati di test
    pred = model.predict(x_test)
    
    # Calcola l'errore quadratico medio tra le previsioni e i dati di test
    mse = mean_squared_error(y_test, pred)
    
    # Restituisci il valore dell'errore quadratico medio
    return mse
    # Puoi rimuovere il commento dalla riga successiva se desideri visualizzare un riassunto del modello
    # print(model.summary())
