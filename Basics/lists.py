# Define a list
student_names = []
student_names = ["Mark", "Katarina", "Jessica"]

# Getting list elements
student_names = ["Mark", "Katarina", "Jessica"]
print(student_names)
print("first element = " + student_names[0])
print("third element = " + student_names[2])
print("last element = " + student_names[-1])  # get LAST element in the list

print()

# Changing a list element
student_names = ["Mark", "Katarina", "Jessica"]
print(student_names)
student_names[0] = "James"
student_names == ["James", "Katarina", "Jessica"]
print(student_names)

print()

# Add to the end of the list
student_names = ["Mark", "Katarina", "Jessica"]
print(student_names)
student_names.append("Homer")
print(student_names)

print()

# Check for existence of a value in a list
print("Mark exists in the list")
print("Mark" in student_names)

print()

# Get number of elements in the list
print("length of list")
print(len(student_names))

print()

# Remove an element from the list
print(student_names)
del student_names[2]
student_names = ["Mark", "Katarina", "Homer"]
print(student_names)

print()

# List slicing
student_names = ["Mark", "Katarina", "Homer"]
print(student_names[1:])  # skip first element of list and return remaining
print(student_names[1:-1])  # ignore both first and last elements of list and return remaining
