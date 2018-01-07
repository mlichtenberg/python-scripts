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
