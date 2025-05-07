#Assignment:
#Create a class Product with a private attribute _price.
#Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage:
p = Product(100)
print(p.price)     # Getter
p.price = 150      # Setter
print(p.price)
del p.price        # Deleter