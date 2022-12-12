import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# creare una funzione per prendere in input i dataset
# far si che in ogni dataset elimini la collonna SNo
# sistemare i dati per ogni dataset
# modificare le maiuscole in minuscole
# normalizzare i dati!!!!
# ------
# questo è il primo oassaggio per sistemare i dati!

errors = []


for filename in glob.glob('C:/Users/stefa/OneDrive/Desktop/esame pierandrei/archive/*.csv'):
    df = pd.read_csv(filename, sep=',', header=0)
    df.drop('SNo', axis = 1, inplace=True)
    df.columns = df.columns.str.lower()
    #print(df.columns)
    # fare preprocessing
    #normalizare i dati 
    # modificare maiuscole in minuscolo
    # modello di regressione!
    # x = np.mean(df.Open, df.Close)
    # x1 = np.mean(df.Low, df.High)
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

    errors.append(m)

    # plt.plot(p, color = 'r')
    # plt.plot(X_test, alpha = .2)
    # plt.show()

    # dividere 70-30 train, test
    # fare grafico
    # regressione lineare
    # plt.scatter(x =df.index, y = df.close)
    # plt.show()
    fileoutputname = 'archive/output.txt'


print(errors)

with open(fileoutputname, 'w') as f:
    outputstring = ""
    for i, error in enumerate(errors):
        outputstring += f'file {i + 1}, errore: {error}\n'
    f.write(outputstring)