import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
df = pd.read_csv('crypto_prices.csv')
# Drop any rows with missing values
df.dropna(inplace=True)
# Select the "Close" column as the target variable
y = df['Close']
# Drop the "Close" column and use the remaining columns as the input features
X = df.drop(columns=['Close'])
# Scale the input features using MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
# Split the data into training and test sets
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]
# Build the model
model = Sequential()
model.add(Dense(50, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

# Evaluate the model on the test data
score = model.evaluate(X_test, y_test, verbose=0)
print('Test MSE:', score)
