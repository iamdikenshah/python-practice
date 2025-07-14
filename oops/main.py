# 1. Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls Animal's __init__
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()  # Calls Animal's speak
        return f"{parent_sound} and Woof!"

# Example usage:
dog = Dog("Bruno", "Labrador")
print(dog.name)      # Bruno
print(dog.breed)     # Labrador
print(dog.speak())   # Some sound and Woof!


# 2. Multiple Inheritance
class Father:
    def skills(self):
        return "Gardening"

class Mother:
    def skills(self):
        return "Cooking"

class Child(Father, Mother):
    def skills(self):
        return "Dancing"

# 3. Multilevel Inheritance
class Grandparent:
    def show(self):
        return "Grandparent"

class Parent(Grandparent):
    pass

class Child2(Parent):
    pass

# 4. Hierarchical Inheritance
class Bird(Animal):
    def speak(self):
        return "Chirp!"

class Fish(Animal):
    def speak(self):
        return "Blub!"

# 5. Hybrid Inheritance (combination of multiple and hierarchical)
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Example usage:
dog = Dog("Bruno", "Labrador")
print(dog.speak())  # Woof!

child = Child()
print(child.skills())  # Gardening (Father's skills, due to MRO)

child2 = Child2()
print(child2.show())  # Grandparent

bird = Bird("Parrot")
print(bird.speak())  # Chirp!

fish = Fish("Goldfish")