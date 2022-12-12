import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# creare una funzione che mi permetta di fare diverse cose:
# fare minimo due/tre funzioni
# una per sistemare i dati in ogni dataset, una per applicare l'algoritmo 
# una finale per prendere il minore e il maggiore e studiare i grafici solo di quei due!

# normalizzare i dati

errors = []


for filename in glob.glob('C:/Users/StefanoPerdicchia/Crypto_regression/archive/*.csv'):
    df = pd.read_csv(filename, sep=',', header=0)
    df.drop('SNo', axis = 1, inplace=True)
    df.columns = df.columns.str.lower()
    # normalizzazione dei dati

    #print(df.columns)
    # fare preprocessing
    #normalizare i dati 
    # modificare maiuscole in minuscolo
    # modello di regressione!
    # x = np.mean(df.Open, df.Close)
    # x1 = np.mean(df.Low, df.High)
    
    # modello...
    X = np.array([df.open, df.low, df.high])
    X = X.transpose()
    y = df.close
    print(X.shape)
    print(y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, shuffle=None)
    model = LinearRegression()
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    # print(p)
    m = mean_absolute_error(y_test,p)
    print(m)
# provare a programmare una regressione lineare from scratch, quindi fatta da me
# provare a capire come funziona la LASSO regression che magari può essere implementata all'interno del codice su una funzione tutta sua!
    errors.append(m)

    # plt.plot(p, color = 'r')
    # plt.plot(X_test, alpha = .2)
    # plt.show()

    # dividere 70-30 train, test (oppure farlo 80-20)
    # vedere cosa viene meglio
    # fare grafico
    # regressione lineare
    plt.scatter(x =df.index, y = df.close)
    plt.xlabel('...!!!')
    plt.ylabel('???')
    plt.show()
    # nel plot andare a creare le label per dare i nomi a x e y!
    fileoutputname = 'C:/Users/StefanoPerdicchia/Crypto_regression/output.txt'

print(errors)

with open(fileoutputname, 'w') as f:
    outputstring = ""
    for i, error in enumerate(errors):
        outputstring += f'file {i + 1}, errore: {error}\n'
    f.write(outputstring)

    # andare a vedere il file con meno e con piu errore, i motivi ecc!
    