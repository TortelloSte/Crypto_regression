# Analisi dei dati storici di Bitcoin:
Bitcoin è una moneta digitale decentralizzata che ha acquisito popolarità negli ultimi dieci anni.
Poiché il prezzo del Bitcoin è fluttuato in modo drammatico, c'è un crescente interesse nell'utilizzo di tecniche di machine learning  per analizzare e prevedere il prezzo del Bitcoin.
In questo progetto, sono andato ad analizzare i dati storici di bitconi utilizzando differenti metodi e modelli di regressione. Lo scopo ultimo di questo progetto è mostrare come questi dati possano essere studiati attraverso il machine Learning.
Tutti i dati che sono stati utilizzati per questo progetto si possono trovare direttamente al seguente link:
https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory , dal quale si può estrarre il dataset coin_Bitcoin.csv.

Questo studio viene dunque condotto mediante l'utilizzo di python come linguaggio di programmazione per l'implementazione di modelli di Machine Learning, e nel progetto verranno spiegati gli aspetti teorici che si trovano dietro a questi modelli, in maniera tale da poter essere utilizzati per studiare e comprendere i differenti modelli di *Regressione*. 


# Requirement:
Per poter eseguire il programma sono necessari diverse librerie all'interno della nostra area di lavoro in python, il mio consiglio è quello di sfruttare un enviroment nuovo per lo sviluppo di questo studio, il quale lascio pubblico in maniera tale da permettere a chiunque di modificarlo e migliorare i codici.


Le librerie necessarie per questo studio sono le seguenti:
- pandas
- sklearn
- numpy
- datetime
- matplotlib
- keras

Queste possono essere installate tramite terminale, con i comandi:
pip install 'nome librerie'
conda install 'nome librerie' (se si sfrutta anaconda come env)


# Come utilizzare il progetto:
Il progetto viene suddiviso in due cartelle principali:
1. La cartella denominata 'Version_1' fa rifermento ai codici che sono stati sviluppati durante il corso degli studi e successivamente modificati per rendere i codici maggiormente leggibili ed interpretabili.
- All'interno di questa cartella si trovano tre sotto cartelle che sono cosi suddivide:
      - *CoinMarketCap_Api*: al suo interno si trovano i codici che permetto tramite API di estrapolare i dati interenti a Bitcoin direttamente da internet e aggiornati costantemente. Questo codice è stato inserito per esplorare altri metodi di utilizzo di python e di come i dati possano variare rispetto a quelli presti direttamente da Kaggle.com
      - *LSTM_machine_learning*: Dentro a questa cartella si trova il codice che applica il modello LSTM, il quale è stato una prova di applicazione di un modello particolare che verrà spiegato successivamente.
      - *regression_model*: questa è la cartella principale dove si trovano tutti i codici dei modelli applicati al dataset, inoltre per decisione personale ho deciso di scrivere un codice chiamato main e migliorato per andare a valutare i differenti modelli cosi da capire quale fosse il migliore.
2. La cartella denominata 'Version_2' fa riferimento ai nuovi codici che sono stati testati successivamente al corso di studi e che quindi risultano migliorati.
      - All'interno sono presenti solamente due codici, uno è il main che esegue tutti i calcoli, mentre l'altro è un unico macro codice che implementa tutti i modelli applicati nella cartella Version_1 però ottimizzando i codici stessi per raggiungere una struttura differente e migliore.


Per poter utilizzare il progetto consiglio di clonare l'intero main da github, e successivamente di leggere dettagliatamente il file readme.md cosi da comprendere, visto i fini del progetto, la sezione sottostante che spiega come funzionano i differenti modelli di regressione.
Successivamente aggiungere la cartella data al progetto e scaricare da github i dataset con tutti i dati. 



 ### Modelli di regressione

 # 1.





   # Autore:
   Stefano Perdicchia
