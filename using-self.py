#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these 
#values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name      # Using self to initialize name
        self.marks = marks    # Using self to initialize marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage:
student1 = Student("Osama", 82)
student1.display()