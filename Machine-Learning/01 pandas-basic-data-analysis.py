import pandas as pd  # Dataframe library

# Use pandas to read CSV data
df = pd.read_csv("data/pima-data.csv")   # By default, assumes 1st row has column headers

# Check structure of data (number of rows and columns)
shape = df.shape

print("Shape of the data, expressed as (ROWS, COLUMNS)")
print(shape)
print()

#  View some of the data
head = df.head(5)   # first five rows
tail = df.tail(5)   # last five rows

print("First five rows of data")
print(head)
print()
print("Last five rows of data")
print(tail)
print()

# Check for null values
nulls = df.isnull().values.any()

print("Data contains nulls")
print(nulls)