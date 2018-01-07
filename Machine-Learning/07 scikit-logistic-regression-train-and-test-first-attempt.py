# Import N-dimensional object support
import numpy as np
# Import the performance metrics library.  It includes score functions, performance metrics, and
# pairwise metrics and distance computations.
from sklearn import metrics
# Import the Logistic Regression classifier library
from sklearn.linear_model import LogisticRegression

# Load the clean training and testing data
# The 'X' arrays contain the feature values.  The 'Y' arrays contain the class values.
# So, given the features in row N of the X array, the value in row N of the Y array is the class (outcome).
X_train = np.loadtxt("data/pima-data-clean-x-train.txt", delimiter=",")
Y_train = np.loadtxt("data/pima-data-clean-y-train.txt", delimiter=",")
X_test = np.loadtxt("data/pima-data-clean-x-test.txt", delimiter=",")
Y_test = np.loadtxt("data/pima-data-clean-y-test.txt", delimiter=",")

# Create a Logistic Regression model object and train it with the training data.
# "C" is the Regularization Hyperparameter
#   Helps to "fix" overfitting
#   Controls how well the algorithm covers edge cases of the data
#   Usually some experimentation is needed to find the correct value
#   Set here to 0.7 as a starting guess
# The 'ravel()' function converts the array to a contiguous flattened array.
#   For example, ravel() will conert the array [[1, 2, 3], [4, 5, 6]] into [1 2 3 4 5 6].
lr_model = LogisticRegression(C=0.7, random_state=42)
lr_model.fit(X_train, Y_train.ravel())

# Predict values using the training data
lr_predict_train = lr_model.predict(X_train)

# View the accuracy of the model against the training data.  Y_train are the known class values,
# and lr_predict_train are the predicted class values for the same features.
print("Accuracy against training data: {0:.4f}".format(metrics.accuracy_score(Y_train, lr_predict_train)))
print()

# Predict values using the test data
lr_predict_test = lr_model.predict(X_test)

# View the accuracy of the model against the test data.  Y_test are the known class values,
# and lr_predict_test are the predicted class values for the same features.
print("Accuracy against test data: {0:.4f}".format(metrics.accuracy_score(Y_test, lr_predict_test)))
print()

# View the Confusion Matrix to evaluate the accuracy of the model against the test data.
#
# Returns an array of the form
#		[[True-negative    False-positive]
#		 [False-negative    True-positive]]
#
# A "perfect" classification would have zero values for False-negative and False-positive.
print("Confusion Matrix")
print(metrics.confusion_matrix(Y_test, lr_predict_test) )
print()

# View the Classification Report showing classification metrics for the model against the test data.
# Two key metrics displayed are Recall and Precision.
#	Recall
#		- The true positive rate.
#		- It is how well the model is predicting a true result when the result is actually true.
#		- Mathematically, recall equals the true positive divided by the sum of the true positive plus the false negative.
#		- Increasing this number means more true positives.
#	Precision
#		- Positive predictor value.
#		- This is how often the real world result was positive when the model said it would be.
#		- Mathematically, precision equals true positive, divided by true positive plus false positive.
#		- Increasing this number means fewer false positives.
print("Classification Report")
print(metrics.classification_report(Y_test, lr_predict_test))

# Initially, the scores are an improvement over the previous algorithm, but the recall
# values (true positives) are still lower than desired.  Trying different values for the
# Regularization Hyperparameter ("C" in the LogisticRegression initialization) will likely
# find a better set of results.
