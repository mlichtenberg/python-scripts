# Example
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

# List of dictionaries
all_students = [
    {"name": "Mark", "student_id": 15163 },
    {"name": "Katarina", "student_id": 63112 },
    {"name": "Jessica", "student_id": 30021 }
]

# Get a value from a dictionary
print("student name is " + student["name"])
print("student name is " + student.get("name"))

# Return a default value if a key does not exist
print(student.get("last_name", "Unknown"))

# Get all keys from a dictionary
print(student.keys())

#Get all values from a dictionary
print(student.values())

# Set a dictionary value
student["name"] = "James"
print(student["name"])

# Remove a key from a dictionary
del student["name"]
print(student.get("name", "Unknown"))
