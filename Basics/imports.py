# Import functionality defined in other files into the current file

# Import everything (*) from the file "lambdas"
from lambdas import *

# Import only the "get_students_titlecase" function from the file "functions"
from import_functions import get_students_titlecase

# Call function from the lambdas file
print(double_lambda(10))

# Call function from the functions file
print(get_students_titlecase())

