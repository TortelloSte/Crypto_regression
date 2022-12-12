import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
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


df = pd.read_csv('C:/Users/stefa/OneDrive/Desktop/esame pierandrei/archive/coin_Bitcoin.csv', sep=',', header=0)

df.drop('SNo', axis = 1, inplace=True)
#print(df.columns)
# fare preprocessing
#normalizare i dati 
# modificare maiuscole in minuscolo

# modello di regressione!


# x = np.mean(df.Open, df.Close)
# x1 = np.mean(df.Low, df.High)
X = np.array([df.Open, df.Low, df.High])
X = X.transpose()
y = df.Close
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=None)
model = LinearRegression()
model.fit(X_train, y_train)
p = model.predict(X_test)
# print(p)
m = mean_absolute_error(y_test,p)
print(m)


plt.plot(p, color = 'r')
plt.plot(X_test, alpha = .2)
plt.show()

# dividere 80-20 train, test
# valutare un accuracy
# fare grafico
# regressione lineare
#plt.scatter(x =df.index, y = df.Close)
#plt.show()


