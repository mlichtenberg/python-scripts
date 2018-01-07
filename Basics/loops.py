# Basic loop
student_names = ["Mark", "Katarina", "Jessica"]
for name in student_names:
    print ("Student name is {0}".format(name))

print()

# Range function tells loop to iterate a certain number of times.
# In this example, 10 times.
x = 0
for index in range(10):
    x += 10
    print('the value of X is {0}'.format(x))

print()

# Range function tells loop where to start and end.
# In this example, the index starts at 5 and continues while the index is less than 10.
x = 0
for index in range(5, 10):
    x += 10
    print('the value of X is {0}'.format(x))

print()

# Range function tells loop where to start and end, and the size of the increment.
# In this example, the index starts and five and also interacts over index = 7 and index = 9).
x = 0
for index in range(5, 10, 2):
    x += 10
    print('the value of X is {0}'.format(x))

print()

# Use the break keyword to exit a loop
for index in range(10):
    if index == 5:
        break
    print('the value of index is {0}'.format(index))

print()

# Use the continue keyword to skip the remainder of the loop block and resume with the next iteration
for index in range(10):
    if index < 6:
        continue
    print('the value of the index is {0}'.format(index))

print()

# While loop
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1
