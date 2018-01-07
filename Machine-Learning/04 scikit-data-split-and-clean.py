import pandas as pd  # Dataframe library
import matplotlib as plt   # Plotting library
import numpy as np   # N-dimension object support

# Load the clean data.
# See the pandas* examples to see how the data was cleaned.
df = pd.read_csv("data\pima-data-clean.csv")  # Use pandas to read CSV data

# Load a class from scikit-learn to be used to split the data
# DEPRECIATION WARNING ON THIS MODULE!!! UPDATE CODE TO USE THE model_selection MODULE INSTEAD!!!
from sklearn.cross_validation import train_test_split

# Get the values of the predictor feature columns (8 X m)
feature_col_names = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
X  = df[feature_col_names].values  

# Get the values of the predicted class column (1=true, 0=false) column (1 X m)
predicted_class_names = ['diabetes']
Y = df[predicted_class_names].values  

# Set the size of the data sets in which to split the data (70% for training, 30% for testing)
split_test_size = 0.30

# Split the data.  The value 42 provides a seed for the randomizer, ensuring that the same split can be reproduced in the future.
# Any value can be used.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=split_test_size, random_state=42)

# Confirm that the data is split 70/30
print("{0:0.2f}% in training set".format((len(X_train)/len(df.index)) * 100))
print("{0:0.2f}% in test set".format((len(X_test)/len(df.index)) * 100))
print()

# Confirm that the ratio of true to false outcomes in the data set was preserved when the data was split
print("Original True  : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 1]), (len(df.loc[df['diabetes'] == 1])/len(df.index)) * 100.0))
print("Original False : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 0]), (len(df.loc[df['diabetes'] == 0])/len(df.index)) * 100.0))
print("")
print("Training True  : {0} ({1:0.2f}%)".format(len(Y_train[Y_train[:] == 1]), (len(Y_train[Y_train[:] == 1])/len(Y_train) * 100.0)))
print("Training False : {0} ({1:0.2f}%)".format(len(Y_train[Y_train[:] == 0]), (len(Y_train[Y_train[:] == 0])/len(Y_train) * 100.0)))
print("")
print("Test True      : {0} ({1:0.2f}%)".format(len(Y_test[Y_test[:] == 1]), (len(Y_test[Y_test[:] == 1])/len(Y_test) * 100.0)))
print("Test False     : {0} ({1:0.2f}%)".format(len(Y_test[Y_test[:] == 0]), (len(Y_test[Y_test[:] == 0])/len(Y_test) * 100.0)))

# Post-split data preparation (must be applied to both training and test data sets)
# In these sets of example data, zero values are invalid.
# Look for invalid zero values
print()
print("# rows in dataframe {0}".format(len(df)))
print("# rows missing glucose_conc: {0}".format(len(df.loc[df['glucose_conc'] == 0])))
print("# rows missing diastolic_bp: {0}".format(len(df.loc[df['diastolic_bp'] == 0])))
print("# rows missing thickness: {0}".format(len(df.loc[df['thickness'] == 0])))
print("# rows missing insulin: {0}".format(len(df.loc[df['insulin'] == 0])))
print("# rows missing bmi: {0}".format(len(df.loc[df['bmi'] == 0])))
print("# rows missing diab_pred: {0}".format(len(df.loc[df['diab_pred'] == 0])))
print("# rows missing age: {0}".format(len(df.loc[df['age'] == 0])))

# Impute (replace) all 0 readings (in both training and test data) with the mean value
from sklearn.preprocessing import Imputer

fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)

X_train = fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)


# Show the test and training data
print(X_train)
print()
print(X_test)
print()
print(Y_train)
print()
print(Y_test)

# Write the training and testing data to csv files.
# Use np.loadtxt(FILENAME, delimiter=",") to read the data from the files.
np.savetxt("data/pima-data-clean-x-train.txt", X_train, delimiter=",", fmt="%.3f")
np.savetxt("data/pima-data-clean-y-train.txt", Y_train, delimiter=",", fmt="%.3f")
np.savetxt("data/pima-data-clean-x-test.txt", X_test, delimiter=",", fmt="%.3f")
np.savetxt("data/pima-data-clean-y-test.txt", Y_test, delimiter=",", fmt="%.3f")