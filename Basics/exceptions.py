student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError as error:     # catch a specific type of error (KeyError)
    print("Error finding last_name")
    print(error)
except Exception:      # generic error handler
    print("Unknown error")
    
print("This code executes!")
