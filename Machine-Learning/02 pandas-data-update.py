import pandas as pd  # Dataframe library

# Use pandas to read CSV data
df = pd.read_csv("data/pima-data.csv")   # By default, assumes 1st row has column headers

#  View some of the data
print("First five rows of data BEFORE updates")
print(df.head(5))
print()

# Delete a column named "skin"
del df['skin']

# A column named "diabetes" contains values "True" and "False".
# Map these values to numeric equivalents, 1 and 0.
diabetes_map = {True: 1, False: 0}

# Change the boolean values in the data set to numeric
df['diabetes'] = df['diabetes'].map(diabetes_map)

print("First five rows of data AFTER updates")
print(df.head(5))
print()

# Write the cleaned-up data to a csv file.
# The 'index' parameter removes row numbers from the output.
# The 'float_format' parameter forces the float values to a particular format.
df.to_csv("data/pima-data-clean.csv", index=False, float_format='%.3f')   # By default, column headers are written
