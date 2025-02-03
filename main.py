# Import the necessary modules
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Read in the file fg_attempt.csv
iris_dataset = pd.read_csv('iris_data.csv')

print (f"{iris_dataset.shape}")
x1Name = 'petal_length'
x2Name = 'petal_width'
x3Name = 'sepal_length'
x4Name = 'sepal_width'
# Create a dataframe X containing 2 features
X = df[[x1Name, x2Name]]
# Create a dataframe y containing 'class'
y = df[[Class]]

# Flatten y into an array
# Your code here
yArray = np.ravel(y)

# Initialize a LogisticRegression() model
logisticModel = # Your code here

# Fit the model
# Your code here

# Input feature values for a sample instance

x1 = float(input())
x2 = float(input())

# Create a new dataframe with user-input Distance and ScoreDiffPreKick
XNew = # Your code here

# Predict the outcome from the new data
pred = # Your code here
print(pred)

# Determine the accuracy of the model logisticModel
score = # Your code here
print(f"{score:.2f}")

