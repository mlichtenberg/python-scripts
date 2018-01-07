# Note that there are no access modifiers (public, private, protected) in Python

# List for functions to use
students = []

# "pass" means "do nothing".  Useful for creating stub functions.
class Car:
    pass

class Student:
    # Static variable (a "class" attribute, not an "instance" attribute)
    school_name = "Springfield Elementary"

    # "__init__" is the function constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    # "__str__" is a built in method called when the object is printed.
    # The __str__ method defined here overrides the default __str__ method.
    def __str__(self):
        return "Student " + self.name

    # "self" is similar to "this" in other languages
    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# Class "HighSchoolStudent" inherits from class "Student"
class HighSchoolStudent(Student):

    # Override class (static) attribute of the base class
    school_name = "Springfield High School"

    # Override method of base class
    def get_school_name(self):
        return "This is a High School student"

    # Override method of base class, while executing base class method
    def get_name_capitalize(self):
        # "super()" refers to the parent/base class
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


mark = Student("Mark")

# __str__ method enables this print statement
print (mark)

# print the static variable (the "class" attribute)
print (Student.school_name)

james = HighSchoolStudent("james")
print(james.get_name_capitalize())
