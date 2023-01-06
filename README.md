# Analisi dei dati storici di Bitcoin:
Bitcoin è una moneta digitale decentralizzata che ha acquisito popolarità negli ultimi dieci anni.
Poiché il prezzo del Bitcoin è fluttuato in modo drammatico, c'è un crescente interesse nell'utilizzo di tecniche di machine learning 
per analizzare e prevedere il prezzo del Bitcoin.
In questo progetto, abbiamo analizzato i dati storici di Bitcoin utilizzando diversi modelli di regressione
Tutti i dati sono reperibili al seguente link: https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory , estraendo dal file il dataset coin_Bitcoin.csv.
    
# Requirement:
Per poter eseguire il programma sono necessari diverse librerie all'interno della nostra area di lavoro in python, 
infatti le librerie necessarie da installare sono:
- pandas
- sklearn
- numpy
- datetime
- matplotlib\
Possiamo notare come i file siano divisi in diverse cartelle, questo perchè sono stati utilizzati diversi metodi di Regressione, per quanto riguarda l'esame, esiste la cartella apposta (per il corso Data Modelling in ITS). 

# Come utilizzare il progetto:
1- Scarica i dati di input dal link citato sopra (per il file LSTM i dati sono privati, quindi da richiedere!)\
2- scaricare la cartella esame, inserire al suo interno il dataset estratto precedentemente, eseguire il Main.\
3- Per utilizzare il file di Coinmarketcap, recarsi sul sito: https://coinmarketcap.com/api/, creare un profilo e nel codice inserire la propria chiave API, fatto questo il modello inserirà in un file i dati riguardati la criptovaluta scelta, per poter estrarre dunque i dati storici\
4- il modello LSTM ivece risulta particolare, quindi si trova a questa pagina la documentazione: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

 Infine vorrei citare:
durante lo studio è stato eseguito molteplici volte la rete neurale che ci ha dato risultati non 
soddisfacenti in mancanza di dati sufficienti, inoltre la regressione linare applicata all'inizio risulta ancora 
il modello migliore per la predizione dei dati.
Questi dati pero sono stati influenzati da situazioni esterne che influenzano il mercato azionario.
    
   # Autore:
   Stefano Perdicchia
