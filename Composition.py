#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car 
#class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start_engine(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        self.engine.start_engine()  # Accessing Engine's method via Car

# Example usage:
engine = Engine()
car = Car(engine)
car.start_car()