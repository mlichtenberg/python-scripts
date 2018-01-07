# Import N-dimensional object support
import numpy as np
# Import the performance metrics library.  It includes score functions, performance metrics, and
# pairwise metrics and distance computations.
from sklearn import metrics
# Import the Gaussian Naive Bayes algorithm library
from sklearn.naive_bayes import GaussianNB

# Load the clean training and testing data
# The 'X' arrays contain the feature values.  The 'Y' arrays contain the class values.
# So, given the features in row N of the X array, the value in row N of the Y array is the class (outcome).
X_train = np.loadtxt("data/pima-data-clean-x-train.txt", delimiter=",")
Y_train = np.loadtxt("data/pima-data-clean-y-train.txt", delimiter=",")
X_test = np.loadtxt("data/pima-data-clean-x-test.txt", delimiter=",")
Y_test = np.loadtxt("data/pima-data-clean-y-test.txt", delimiter=",")

# Create a Gaussian Naive Bayes model object and train it with the training data.
# The 'ravel()' function converts the array to a contiguous flattened array.
#   For example, ravel() will conert the array [[1, 2, 3], [4, 5, 6]] into [1 2 3 4 5 6].
nb_model = GaussianNB()
nb_model.fit(X_train, Y_train.ravel())

# Example of testing the Naïve Bayes model

# Predict values using the training data
nb_predict_train = nb_model.predict(X_train)

# View the accuracy of the model against the training data.  Y_train are the known class values,
# and nb_predict_train are the predicted class values for the same features.
print("Accuracy against training data: {0:.4f}".format(metrics.accuracy_score(Y_train, nb_predict_train)))
print()

# Predict values using the testing data
nb_predict_test = nb_model.predict(X_test)

# View the accuracy of the model against the test data.  Y_test are the known class values,
# and nb_predict_test are the predicted class values for the same features.
print("Accuracy against test data: {0:.4f}".format(metrics.accuracy_score(Y_test, nb_predict_test)))
print()

# View the Confusion Matrix to evaluate the accuracy of the model against the test data.
#
# Returns an array of the form
#		[[True-negative    False-positive]
#		 [False-negative    True-positive]]
#
# A "perfect" classification would have zero values for False-negative and False-positive.
print("Confusion Matrix")
print("{0}".format(metrics.confusion_matrix(Y_test, nb_predict_test)))
print("")

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
print(metrics.classification_report(Y_test, nb_predict_test))
