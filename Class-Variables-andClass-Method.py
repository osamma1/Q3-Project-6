#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
#that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"{self.account_holder} - Bank: {Bank.bank_name}")

# Example usage:
acc1 = Bank("Osama")
acc2 = Bank("Hammad")

acc1.display()
acc2.display()

# Change the bank name
Bank.change_bank_name("Future Bank")

acc1.display()
acc2.display()