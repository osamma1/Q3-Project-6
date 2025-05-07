#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet() method returning 
#"Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"  # Adding greet method
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage:
person = Person("Osama")
print(person.greet())  # "Hello from Decorator!"