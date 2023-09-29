# Importa le librerie necessarie
import numpy as np
import pandas as pd
import datetime as dt

# Definisci una funzione chiamata 'datas' che accetta il percorso del file CSV come parametro
def datas(path):
    # Leggi i dati dal file CSV specificato nel percorso
    data = pd.read_csv(path)

    # Rimuovi alcune colonne non necessarie dal DataFrame
    data.drop(columns=["Name", "SNo", "Symbol", "Marketcap", "Volume"], axis=1, inplace=True)

    # Converti la colonna 'Date' in formato datetime
    data["Date"] = pd.to_datetime(data["Date"])

    # Estrai l'anno, il mese e il giorno dalla colonna 'Date' e crea nuove colonne per essi
    data['Date_year'] = data["Date"].dt.year
    data['Date_month'] = data["Date"].dt.month
    data['Date_day'] = data["Date"].dt.day
    # Rimuovi la colonna 'Date', se presente, in modo da avere solo le colonne di anno, mese e giorno
    data.drop(columns=["Date"], axis=1, inplace=True)

    # Rimuovi le righe che contengono valori mancanti (NaN)
    data.dropna(inplace=True)

    # Restituisci il DataFrame risultante
    return data
