from decision_tree import decision_tree_model
from deep_learning_model import modello_rete_neurale
from regressione_lineare import regression_model

# Percorso del file dati
data_file_path = "./DATA/archive/coin_Bitcoin.csv"

# Esegui la funzione regression_model e salva l'errore medio assoluto ottenuto
mae_regressione = regression_model(data_file_path)

# Esegui la funzione decisiontree e salva l'errore medio assoluto ottenuto
mae_decisiontree = decision_tree_model(data_file_path)

# Esegui la funzione modello_rete e salva l'errore quadratico medio ottenuto
mse_modello_rete = modello_rete_neurale(data_file_path)

# Confronta i risultati dei modelli
print("Errore Medio Assoluto (Regressione Lineare):", mae_regressione)
print("Errore Medio Assoluto (Albero Decisionale):", mae_decisiontree)
print("Errore Quadratico Medio (Rete Neurale):", mse_modello_rete)

# Concludi quale modello ha ottenuto l'errore più basso
if mae_regressione < mae_decisiontree and mae_regressione < mse_modello_rete:
    print("Il modello di Regressione Lineare ha l'errore medio assoluto più basso.")
elif mae_decisiontree < mae_regressione and mae_decisiontree < mse_modello_rete:
    print("Il modello di Albero Decisionale ha l'errore medio assoluto più basso.")
else:
    print("Il modello di Rete Neurale ha l'errore quadratico medio più basso.")
