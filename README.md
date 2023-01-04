# Crypto_regression
    Bitcoin è una moneta digitale decentralizzata che ha acquisito popolarità negli ultimi dieci anni. Poiché il prezzo del Bitcoin è fluttuato in modo drammatico, c'è un crescente interesse nell'utilizzo di tecniche di machine learning per analizzare e prevedere il prezzo del Bitcoin.
    Il seguente lavoro vuole essere un progetto per andare a fare predizioni sui prezzi delle cryptovalute, nel particolare di Bitcoin stesso partendo dai loro prezzi storici, tutti questi dati sono accessibili presso il seguente link: 
        https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory.
    
    Nel caso del nostro programma dalla cartella andiamo ad estrarre un solo dataset, nel nostro caso appunto andiamo ad estrapolare il file coin_Bitcoin.it

    Per poter eseguire il programma sono necessari diverse librerie all'interno della nostra area di lavoro in python, infatti le librerie necessarie da installare sono:
    - pandas
    - sklearn
    - numpy
    - datetime
    - matplotlib

    In questo progetto, abbiamo utilizzato una rete neurale e un Decision Tree per analizzare i dati del Bitcoin. La rete neurale, implementata utilizzando la funzione sequential() della libreria keras, è stata addestrata su un dataset di prezzi storici del Bitcoin. Il Decision Tree è stato addestrato sullo stesso dataset. Per valutare le prestazioni dei modelli, abbiamo diviso il dataset in un insieme di training e un insieme di test. La rete neurale e il regressore ad albero di decisione sono stati entrambi addestrati sull'insieme di training e quindi testati sull'insieme di test.

     Infine vorrei citare:
    durante lo studio è stato eseguito molteplici volte la rete neurale che ci ha dato risultati non soddisfacenti in mancanza di dati sufficienti, inoltre la regressione linare applicata all'inizio risulta ancora il modello migliore per la predizione dei dati.
    Questi dati pero sono stati influenzati da situazioni esterne che influenzano il mercato azionario.