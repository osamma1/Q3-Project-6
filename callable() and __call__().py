#Assignment:
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that 
#multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Example usage:
m = Multiplier(5)
print(callable(m))      # True, because __call__ is defined
print(m(10))            # 50 (5 * 10)
print(callable(m(10)))  # False, because m(10) returns an int, not a callable
# The callable() function checks if an object appears callable (i.e., can be called as a function).