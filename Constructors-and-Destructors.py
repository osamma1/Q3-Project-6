#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another 
#message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

# Example usage:
log = Logger()

# You can optionally delete the object manually
del log