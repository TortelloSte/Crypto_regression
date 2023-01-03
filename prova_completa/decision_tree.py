from file_opening import datas
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def decisiotree(filepath):
    y= datas(filepath)["Close"]
    x = datas(filepath).drop(["Close", "Date_year",'Date_month','Date_day'], axis= 1)
    x_train, x_test, y_train, y_test= train_test_split(x, y, shuffle=True, test_size = 0.1)
    albero =DecisionTreeRegressor(max_depth=10, min_samples_leaf= 3)
    albero.fit(x_train, y_train)
    ypredd=albero.predict(x_test)
    mae = mean_absolute_error(y_test, ypredd)
    print(mae)
    # printato!