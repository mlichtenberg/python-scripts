import os

# Write (append) data to a file
# Files can be accessed several different ways:
#   "r" = read
#   "w" = write
#   "a" = append
#   "rb" = read binary
#   "wb" = write binary
student = "mike"
f = open("students.txt", "a")     # "a" opens the file to append data
f.write(student + "\n")
f.close()

# Read data from a file
try:
    f = open("students.txt", "r")
    for student in f.readlines():
        print(student)
    f.close()
except Exception:
    print("Could not read file")

# Remove a file
os.remove("students.txt")
