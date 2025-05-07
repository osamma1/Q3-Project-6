#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object 
#store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department has an Employee

    def display(self):
        print(f"Department: {self.department_name}")
        self.employee.display()  # Accessing Employee's method via Department

# Example usage:
emp = Employee("Osama", "Cyber Security Analyst")
dept = Department("IT", emp)
dept.display()