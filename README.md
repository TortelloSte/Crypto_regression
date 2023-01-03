# Crypto_regression
    Il seguente lavoro vuole essere un progetto per andare a fare predizioni sui prezzi delle cryptovalute partendo dai loro prezzi storici, tutti questi dati sono accessibili presso il seguente link: 
        https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory

    Per poter eseguire il programma sono necessari diverse librerie all'interno della nostra area di lavoro in python, infatti le librerie necessarie da installare sono:
    - glob
    - pandas
    - sklearn
    - (da completare la lista)

    Il progetto viene suddiviso in tre parti principali, una prima dove si vanno a fare le analisi del dataset (in totale sono 23 dataset), dove andiamo a rimuovere una colonna, controlliamo che i dati siano corretti e non siano presenti dei valori nulli e infine andiamo a graficare tutti i dati presenti per poter vedere in maniera visiva quali sono i nostri dati.
    Successivamente si è deciso di applicare un modello di ML di Regressione, ossia un DecisioTree.
    Infine dopo aver applicato questo modello andiamo a vedere se sono presenti delle predizioni attendibili per il nostro modello.

    -- Prima di applicare questo modello è stato applicato un modello di regressione linare, ma visto che sembrava troppo "semplice" applicare un modello del genere su questo tipo di dati, si è deciso di implementare un modello di DecisionTree Regressor!
