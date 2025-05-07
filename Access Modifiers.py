#Assignment:
#Create a class Employee with:

#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.

#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN (Private):", self.__ssn)

# Example usage:
emp = Employee("Osama", 500000, "123-45-6789")

# Accessing variables
print("Public:", emp.name)            # Works
print("Protected:", emp._salary)      # Works (not recommended directly)
# print("Private:", emp.__ssn)        # Error: Cannot access directly

# Correct way to access private variable (optional demonstration)
print("Private (via name mangling):", emp._Employee__ssn)