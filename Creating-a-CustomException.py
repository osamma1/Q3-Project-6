#Assignment:
#Create a custom exception InvalidAgeError. Write
#a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You are underage!")
    else:
        print("Access granted.")

# Example usage:
try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)