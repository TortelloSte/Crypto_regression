# Importa la funzione 'datas' dal modulo 'file_opening'
from file_opening import datas
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Definisci una funzione 'decisiontree' che accetta un percorso del file come argomento
def decision_tree_model(filepath):
    # Estrai il target (Close) dai dati utilizzando la funzione 'datas'
    y = datas(filepath)["Close"]
    
    # Estrai le caratteristiche (features) dal DataFrame e rimuovi alcune colonne non necessarie
    x = datas(filepath).drop(["Close", "Date_year", 'Date_month', 'Date_day'], axis=1)
    
    # Dividi i dati in un set di addestramento (train) e un set di test
    x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.1)
    
    # Crea un modello di regressione basato su albero decisionale
    albero = DecisionTreeRegressor(max_depth=10, min_samples_leaf=3)
    
    # Addestra il modello sugli dati di addestramento
    albero.fit(x_train, y_train)
    
    # Effettua previsioni sui dati di test
    y_pred = albero.predict(x_test)
    
    # Calcola l'errore medio assoluto tra le previsioni e i dati di test
    mae = mean_absolute_error(y_test, y_pred)
    
    # Restituisci il valore dell'errore medio assoluto
    return mae
