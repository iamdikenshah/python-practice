# Args and kwargs in Python allow you to pass a variable number of arguments to a function.
# *args allows you to pass a variable number of positional arguments,
# while **kwargs allows you to pass a variable number of keyword arguments.



def my_function(*args):
    print(type(args)) # <class 'tuple'>
    for arg in args:
        print(arg)


my_function(1, 2, 3, "hello") # Output: 1 2 3 hello
my_function() # No output (empty tuple)
my_function("a", "b") # Output: a b



def my_function(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

my_function() # No output (empty dictionary)
my_function(a=1, b=2)
# Output:
# a: 1
# b: 2


def my_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")  # args is a tuple
    print(f"c: {kwargs.get('c', 10)}")  # Default value for c is 10
    print(f"kwargs: {kwargs}")  # kwargs is a dictionary


my_function(1, 2, 3, 4, 5, c=20, name="Bob", country="USA")
# Output:
# a: 1
# b: 2
# args: (3, 4, 5)
# c: 20
# kwargs: {'name': 'Bob', 'country': 'USA'}
my_function(1,2)
# Output:
# a: 1
# b: 2
# args: ()
# c: 10
# kwargs: {}



# Example showing use in inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed, *args,**kwargs):
        super().__init__(name)
        self.breed = breed
        # Process any additional arguments or keyword arguments here
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")

        
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador", 1,2,3, color="Black", age = 5)