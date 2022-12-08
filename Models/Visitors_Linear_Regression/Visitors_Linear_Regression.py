import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing


def make_dataframe(days=31):
    data = {
        "day": [i for i in range(1, days + 1) for _ in range(24)] * 4,
        "hour": [i for i in range(0, 24) for _ in range(4)] * days,
        "quarter": [i for i in range(1, 5)] * days * 24,
    }
    df = pd.DataFrame(data)
    return df


df = make_dataframe(300)

# make dummy values:
# 0:00-9:00: between 1 and 10
# 9:00-17:00: between 50 and 100
# 17:00-24:00: between 10 and 50
for hour in range(0, 9):
    df.loc[df["hour"] == hour, "value"] = np.random.randint(1, 10)
for hour in range(9, 17):
    df.loc[df["hour"] == hour, "value"] = np.random.randint(50, 100)
for hour in range(17, 24):
    df.loc[df["hour"] == hour, "value"] = np.random.randint(10, 50)

# creating feature variables
X = df.drop("value", axis=1)
y = df["value"]
print("Features:\n\n", X)
print("\nTarget values:\n\n", y)

# creating train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# creating a regression model
model = LinearRegression()
print("\nModel used:", model)

# fitting the model
model.fit(X_train, y_train)

# making predictions
predictions = model.predict(X_test)

# model evaluation
print("\nModel evaluation:")
print("\nmean_squared_error:", mean_squared_error(y_test, predictions))
print("\nmean_absolute_error: ", mean_absolute_error(y_test, predictions))

# create test_data to predict on
test_data = np.array([1, 14, 1])
print(
    "\nMaking prediction with the following input: \nDay:",
    test_data[0],
    "\nHour:",
    test_data[1],
    "\nQuarter:",
    test_data[2],
)

# reshape before prediction
test_data = test_data.reshape(1, -1)
new_pred = model.predict(test_data)
print("\nPredicted value:", new_pred[0])
