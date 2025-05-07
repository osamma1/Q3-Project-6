#Assignment:
#Create four classes:

#A with a method show(),

#B and C that inherit from A and override show(),

#D that inherits from both B and C.

#Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass  # No need to override, will follow MRO

# Example usage:
d = D()
d.show()  # Method Resolution Order (MRO) decides which method is called