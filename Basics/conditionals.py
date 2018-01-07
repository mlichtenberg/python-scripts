# Basic If/Then/Else
number = 5
if number == 5:
    print ("Number is 5")
else:
    print("Number is NOT 5")
    
# Check number variable for truthiness    
number = 5
if number:
    print("Number is defined and truthy")
    
# Check string variable for truthiness
text = "Python"
if text:
    print("Text is defined and truthy")

# Boolean variable evaluation
python_course = True
if python_course:
    print("This will execute")

# None in python is similar to null in other languages
aliens_found = None
if aliens_found:
    print("This will NOT execute")

# Not equal operator
number = 5
if number != 5:
    print("This will not execute")

# Not operator applied to a boolean variable
python_course = True
if not python_course:
    print("This will also not execute")

# AND and OR operators
number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")
if number == 17 or python_course:
    print("This will also execute")

# Ternary if    
a = 1
b = 2
print("bigger") if a > b else print("smaller")
