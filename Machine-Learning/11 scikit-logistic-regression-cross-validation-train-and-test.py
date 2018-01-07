# Import N-dimensional object support
import numpy as np
# Import the performance metrics library.  It includes score functions, performance metrics, and
# pairwise metrics and distance computations.
from sklearn import metrics
# Import the Logistic Regression Cross Validation classifier library
from sklearn.linear_model import LogisticRegressionCV

# Load the clean training and testing data
# The 'X' arrays contain the feature values.  The 'Y' arrays contain the class values.
# So, given the features in row N of the X array, the value in row N of the Y array is the class (outcome).
X_train = np.loadtxt("data/pima-data-clean-x-train.txt", delimiter=",")
Y_train = np.loadtxt("data/pima-data-clean-y-train.txt", delimiter=",")
X_test = np.loadtxt("data/pima-data-clean-x-test.txt", delimiter=",")
Y_test = np.loadtxt("data/pima-data-clean-y-test.txt", delimiter=",")

# When training a model without Cross Validation, checking the accuracy of the model with the
# test data affects the result.  The model ends up being tuned to the test data, and may not
# perform as well against real-world data.
#
# Cross Validation is a training method that avoids the use of the test data.  Instead, the 
# training data is used for all validation.  In the end, Cross Validation many not perform 
# quite as well against a specific set of testing data, but in general should perform better 
# against real-world data.
#
# K-fold Cross Validation
#   Process
#       1) Split the training data into ten "folds", each of the same size
#       2) Select the first fold to be the "validation" set; the others are the training set
#       3) Train the algorithm on the training set and evaluate it with the fold that is the validation set
#       4) Repeat the training and evaluation with the second fold as the validation set
#       5) Continue until each of the folds has been used as the validation data
#   The result of each loop is a set of values for each parameter and associated scores for the accuracy and other performance metrics
#   This provides the capability to generate multiple values with which to tune the hyperparameters
#   A procedure can be written to determine the best value of a hyperparameter for each fold
#   When all of the folds have been processed, the hyperparameter for the model can be set to the average of the fold's best hyperparameter values
#   This provides a model with a hyperparameter that may not perform best on a specific fold or other subset of data but in general performs well on all data
#
# The scikit-learn toolkit includes classes that implement Cross Validation variants
# of the learning algorithms.  Initialization parameters for these variants include
# the number of Folds ("K") and how to determine the optimal value for Hyperparameters.
# Otherwise, the Cross Validation variants are used just like the non-Cross Validation
# versions.

# Create a Logistic Regression Cross Validation model object and train it with the training data.
# LogisticRegressionCV - creates the model
#   n_jobs - number of CPU cores to use; specify -1 to use all available cores
#   random_state - seed value for the random number generator
#   Cs - number of values to be tried as a Regularization Parameter for each fold
#   cv - number of Folds to use for Cross Validation
#   refit - False to use the averaged coefs/intercepts/C that coorespond to the best scores across folds
#           True to do a final refit using averaged scores across all folds and the coefs/C that correspond to the best score
#   class_weight - specify 'balanced' to compensate for unbalanced classes
lr_cv_model = LogisticRegressionCV(n_jobs=1, random_state=42, Cs=3, cv=10, refit=False, class_weight="balanced")
lr_cv_model.fit(X_train, Y_train.ravel())

# Predict values using the training data
lr_cv_predict_train = lr_cv_model.predict(X_train)

# View the accuracy of the model against the training data.  Y_train are the known class values,
# and lr_cv_predict_train are the predicted class values for the same features.
print("Accuracy against training data: {0:.4f}".format(metrics.accuracy_score(Y_train, lr_cv_predict_train)))
print()

# Predict values using the test data
lr_cv_predict_test = lr_cv_model.predict(X_test)

# View the accuracy of the model against the test data.  Y_test are the known class values,
# and lr_cv_predict_test are the predicted class values for the same features.
print("Accuracy against test data: {0:.4f}".format(metrics.accuracy_score(Y_test, lr_cv_predict_test)))
print()

# View the Confusion Matrix to evaluate the accuracy of the model against the test data.
#
# Returns an array of the form
#		[[True-negative    False-positive]
#		 [False-negative    True-positive]]
#
# A "perfect" classification would have zero values for False-negative and False-positive.
print("Confusion Matrix")
print(metrics.confusion_matrix(Y_test, lr_cv_predict_test))
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
print(metrics.classification_report(Y_test, lr_cv_predict_test))
print()

# The recall score is not quite what was achieved by tuning the Regularization Parameter against the 
# test data (see scripts 07, 08, 09, and 10).  However, by using cross validation, the model will likely
# score better on real-world data.  In addition, further tuning with the many LogisicRegressionCV 
# parameters may push the scores a bit higher.
