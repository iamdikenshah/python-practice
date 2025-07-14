# Class Object Example
# This code defines a class `Employee` with attributes and methods to display employee information.
# It then creates instances of the class and displays their information.   

class Employee:
    name = ""
    salary = 0.0
    department = ""

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def displayInformation(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
         
diken = Employee("Diken", 450000, "Engineering")  # Creating an instance of Employee
diken.displayInformation()  # Displaying the information of the employee 

harshil = Employee("Harshil", 500000, "Marketing")  # Creating another instance of Employee
harshil.displayInformation()  # Displaying the information of the second employee


# Constructor Example
# This code defines a class `ConstructorExample` with a constructor that initializes attributes.
# It then creates an instance of the class and displays its attributes.
class Constructor:
    name = "" # Class attribute for name
    age = 0
    department = None  # Default value for department

    def __init__(self, name, age, department = None):
        self.name = name
        self.age = age
        self.department = department  # Initializing department attribute)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")  # Displaying the attributes


meet = Constructor("Meet", 30)  # Creating an instance of Constructor
meet.display()  # Displaying the attributes of the instance

# Instance attributes can be added dynamically
meet.salary = 60000  # Adding a new attribute to the instance
print(f"Name: {meet.name}, Age: {meet.age}, Salary: {meet.salary}")  # Displaying the attributes including the new one

dipak = Constructor("Dipak", 28, "Finance")  # Creating another instance of Constructor
dipak.display()  # Displaying the attributes of the second instance

# Object introspection
# This code demonstrates how to inspect an object's attributes and methods using built-in functions.
print("Attributes of meet:", dir(meet))  # Displaying the attributes and methods of the `meet` instance
