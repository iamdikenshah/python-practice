name = "My name is Diken Shah"
length = len(name)

print(length)

multi_line = '''Hey this is my multi line string
You can write anything here
This is a multi-line string example'''

length = len(multi_line)
print(multi_line)
print(length)

slice = name[0:len(name)]  # Slicing the first 4 characters
print(slice)

print("\n\nString methods:")
print(name.upper()) # Output: " HELLO WORLD "
print(name.lower()) # Output: " hello world "
print(name.strip()) # Output: "hello world"
print(name.replace("Diken", "Pooja")) # Output: " hello Python "
print(name.split()) # Output: ['hello', 'world']

text = " hello world "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"

text = "Python is fun"
print(text.find("is")) # Output: 7
print(text.replace("fun", "awesome")) # Output: "Python is awesome"

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text) # Output: "apple - banana - orange"

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False

print(ord('A')) # Output: 65
print(chr(65)) # Output: 'A'