# List used by functions
student_list = ["mike", "kate", "will", "sarah"]

# Function definition
def get_students_titlecase():
    students_titlecase = []
    for student in student_list:
        students_titlecase.append(student.title())
    return students_titlecase
    
# Function definition
def add_student(name):
    student_list.append(name)

print(student_list)
add_student("jerry")
print(student_list)
print(get_students_titlecase())
print()

# Dictionary used by function
students = [
    {"name": "Mark", "student_id": 15163, "feedback": None, "pluralsight_subscriber": True },
    {"name": "Katarina", "student_id": 63112, "feedback": None, "pluralsight_subscriber": False  },
    {"name": "Jessica", "student_id": 30021, "feedback": None, "pluralsight_subscriber": False  }
]

# Function with optional argument (note default value for optional argument)
def add_student(name, id=332):
    student = { "name": name, "student_id": id }
    students.append(student)

print(students)
add_student("jerry")
print(students)
print()

# Calling a function with named variables
add_student(name="Mike", id=15)
print(students)
print()

# Function with a variable number of arguments
def add_student_var_args(name, *args):
    student = {}
    student["name"] = name
    if len(args) > 0:
        student["student_id"] = args[0]
    if len(args) > 1:
        student["feedback"] = args[1]
    if len(args)  > 2:
        student["pluralsight_subscriber"] = args[2]
    students.append(student)
    
add_student_var_args("Steve", "Loves Python", None, True)
print(students)
print()

# Function with variable number of named arguments
def add_student_named_var_args(name, **kwargs):
    #print(name)
    #print(kwargs["description"], kwargs["feedback"])
    student = {}
    student["name"] = name
    student["student_id"] = kwargs.get("student_id", 100)
    student["feedback"] = kwargs.get("feedback", None)
    student["pluralsight_subscriber"] = kwargs.get("pluralsight_subscriber", False)
    students.append(student)
    
add_student_named_var_args("Martha", feedback="Loves Python", pluralsight_subscriber=True)
print(students)
print()

# Nested function
def get_students():
    students = ["mark", "james"]
    # This function is defined within the get_students container function
    # It has access to variables defined in the container function ("students")
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase
    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)

get_students()
