"""
In machine learning, Correlated Columns state the same information in a different way
Correlated columns do not add any information about how the data causes changes in the
result. And worse, they can amplify a bias because some algorithms naively treat every
column as being independent and just as important.
"""

import pandas as pd  # Dataframe library
import matplotlib.pyplot as plt   # Plotting library

# Use pandas to read CSV data
df = pd.read_csv("data/pima-data.csv")   # By default, assumes 1st row has column headers

# Function for finding correlated value (uses matplotlib)
def plot_corr(df, size=11):
    """
    Plots a graphical correlation matrix for each pair of columns in the dataframe

    Input:
        df: pandas dataframe
        size: vertical and horizontal size of the plot

    Displays:
        matrix of correlation between columns:
        Blue-cyan-yellow-red-darkred => less to more correlated
        0 -----------------------------> 1
        Expect a darkred line running from top left to bottom right
    """

    corr = df.corr()    # data from correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)    # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)    # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)    # draw y tick marks
    plt.show()

# Show the plot of correlated values
plot_corr(df)

# Show the raw correlation values.  Notice that correlated columns "thickness" and "skin" have the same values.
corr = df.corr()
print()
print("Raw correlation values")
print(corr)
