class Person:
    def __init__(self, name):
        self._name = name  # _name is a "protected" attribute

    # Getter method
    def get_name(self):
        return self._name

    # Setter method
    def set_name(self, name):
        self._name = name

# Example usage
person = Person("Alice")
print(person.get_name())  # Alice

person.set_name("Bob")
print(person.get_name())  #

print("-----------------------------------------------------------------")
# Complex example
# ----------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance  # "Protected" attribute

    # Getter for balance
    def get_balance(self):
        return self._balance

    # Setter for balance with validation
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount

    # Getter for owner
    def get_owner(self):
        return self._owner

    # Setter for owner with validation
    def set_owner(self, owner):
        if not owner:
            print("Owner name cannot be empty!")
        else:
            self._owner = owner

# Example usage
account = BankAccount("Alice", 1000)
print(account.get_owner())    # Alice
print(account.get_balance())  # 1000

account.set_balance(1500)
print(account.get_balance())  # 1500

account.set_balance(-500)     # Balance cannot be negative!
print(account.get_balance())  # 1500

account.set_owner("")         # Owner name cannot be empty!