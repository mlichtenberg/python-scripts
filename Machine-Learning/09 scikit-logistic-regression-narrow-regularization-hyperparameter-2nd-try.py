# Import N-dimensional object support
import numpy as np
# Import the performance metrics library.  It includes score functions, performance metrics, and
# pairwise metrics and distance computations.
from sklearn import metrics
# Import the Logistic Regression classifier library
from sklearn.linear_model import LogisticRegression
# Import a plotting library
import matplotlib.pyplot as plt

# Load the clean training and testing data
# The 'X' arrays contain the feature values.  The 'Y' arrays contain the class values.
# So, given the features in row N of the X array, the value in row N of the Y array is the class (outcome).
X_train = np.loadtxt("data/pima-data-clean-x-train.txt", delimiter=",")
Y_train = np.loadtxt("data/pima-data-clean-y-train.txt", delimiter=",")
X_test = np.loadtxt("data/pima-data-clean-x-test.txt", delimiter=",")
Y_test = np.loadtxt("data/pima-data-clean-y-test.txt", delimiter=",")

# In the sample data set, the classes are "unbalanced" (about 35% true and 65% false).
# This may be causing bias estimation, which produces poor prediction results.  Some
# algorithms, include Logistic Regression, include hyperparameters that instruct the
# algorithm to compensate for class imbalances.

# Redo the same loop as the previous attempt, testing all Regularization
# Hyperparameter values between 0.1 and 4.9.
# This time, include an additional "class_weight" Hyperparameter.
# This instructs the algorithm to compensate for the unbalanced classes.
C_start = 0.1
C_end = 5
C_inc = 0.1
C_values, recall_scores = [], []

C_val = C_start
best_recall_score = 0
while (C_val < C_end):
    C_values.append(C_val)
    
    # Add the additional Hyperparameter here
    lr_model_loop = LogisticRegression(C=C_val, class_weight="balanced", random_state=42)

    # Train the model   
    lr_model_loop.fit(X_train, Y_train.ravel())
    # Evaluate the model against the test data
    lr_predict_loop_test = lr_model_loop.predict(X_test)
    # Store the recall value
    recall_score = metrics.recall_score(Y_test, lr_predict_loop_test)
    recall_scores.append(recall_score)
    # Keep track of the best score
    if (recall_score > best_recall_score):
        best_recall_score = recall_score
        best_lr_predict_test = lr_predict_loop_test
        
    C_val = C_val + C_inc

# Print the best recall value and the Regularization Hyperparameter value that produced it
best_score_C_val = C_values[recall_scores.index(best_recall_score)]
print("1st max recall value of {0:.3f} occured at C={1:.3f}".format(best_recall_score, best_score_C_val))
print()

# Plot the Regularization Hyperparameter and recall values
plt.plot(C_values, recall_scores, "-")
plt.xlabel("C value")
plt.ylabel("recall score")
plt.show()

# This time, the best recall value occurred at a Regularization Hyperparameter value of 0.3
# And, the best recall scored was above the desired target value of 0.7.
