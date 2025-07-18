
try:
    x = 10 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")




# Manage multiple exceptions:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
# Alternative using a tuple:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")




try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
    print(f"File contents:\n{content}")
finally:
    file.close()



# Custom exception example
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
def __init__(self, message="Age must be 18 or older!"):
    self.message = message
    super().__init__(self.message)
def verify_age(age):
    if age < 18:
        raise InvalidAgeError() # Raise your custom exception
    return "Welcome!"


try:
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")    