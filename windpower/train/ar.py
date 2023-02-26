import numpy as np
import pandas as pd


# Define the AR model
def ar_model(data, p):
    # Create lag matrix
    X = np.zeros((len(data) - p, p))
    for i in range(p, len(data)):
        X[i - p, :] = data[i - p:i]
    y = data[p:]

    # Estimate coefficients using least squares
    beta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)

    # Predict the next value
    next_value = np.dot(beta, data[-p:])

    return next_value, beta


# Load data from CSV file
data = pd.read_csv("surface_test.csv", header=0)
data = data.iloc[:, 0].values

# Set AR model order
p = 2

# Apply AR model to data
next_value, beta = ar_model(data, p)

# Append predicted value to data and write to output CSV file
output_data = np.append(data, next_value)
pd.DataFrame(output_data).to_csv("output.csv", index=False, header=["Value"])

print("Next value:", next_value)
print("Coefficients:", beta)
