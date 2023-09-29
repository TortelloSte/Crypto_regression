import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Importa la funzione 'datas' dal file 'file_opening' nel modulo 'regression_model' 
from file_opening import datas

# Definisci una funzione 'regress' che accetta un percorso del file come argomento
def regression_model(filepath):
    # Estrai le caratteristiche (features) e il target (Close) dai dati utilizzando la funzione 'datas'
    X = np.array([datas(filepath).Open, datas(filepath).Low, datas(filepath).High])
    X = X.transpose()
    y = datas(filepath).Close

    # Dividi i dati in un set di addestramento (train) e un set di test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=None)
    
    # Crea un modello di regressione lineare
    model = LinearRegression()
    
    # Addestra il modello sui dati di addestramento
    model.fit(X_train, y_train)
    
    # Effettua previsioni sui dati di test
    p = model.predict(X_test)
    
    # Calcola l'errore medio assoluto tra le previsioni e i dati di test
    m = mean_absolute_error(y_test, p)
    
    # Restituisci il valore dell'errore medio assoluto
    return m

# Puoi rimuovere i commenti per le parti di codice che non vuoi visualizzare
# ad esempio, i grafici

# Per visualizzare il grafico, puoi rimuovere i commenti da questo blocco di codice
'''
plt.figure()
plt.plot(datas(filepath)["Date"], p, color='r')
plt.plot(datas(filepath)["Date"].iloc[:y_test.shape[0]:], y_test, alpha=.2)
plt.plot(y)
plt.show()
'''
