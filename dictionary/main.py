dictionary = {"name": "John", "age": 30, "city": "New York", "marks": 85}

print("Dictionary:", dictionary)

print("Adding a new key-value pair:", dictionary.setdefault("country", "USA"))  # Adding a new key-value pair

print("Updated Dictionary:", dictionary)

print("Accessing value for key 'name':", dictionary.get("name"))  # Accessing value using get method

print("Accessing value for key 'country':", dictionary.get("country"))  # Accessing value for a key that exists

print("Accessing value for key 'state':", dictionary.get("state", "Not Found"))  # Accessing value for a key that does not exist

print("Keys in the dictionary:", dictionary.keys())  # Getting all keys

print("Values in the dictionary:", dictionary.values())  # Getting all values

print("Items in the dictionary:", dictionary.items())  # Getting all key-value pairs        

print("Checking if key 'age' exists:", "age" in dictionary)  # Checking if a key exists

print("Checking if key 'country' exists:", "country" in dictionary)  # Checking if a key exists

print("Checking if key 'state' exists:", "state" in dictionary)  # Checking if a key exists

print("Removing key 'city':", dictionary.pop("city", "Not Found"))  # Removing a key-value pair

print("Updated Dictionary after removal:", dictionary)

print("Clearing the dictionary...")
dictionary.clear()  # Clearing the dictionary

print("Dictionary after clearing:", dictionary)  # Displaying the cleared dictionary

print("Re-initializing the dictionary with new values...")

dictionary = {"name": "Alice", "age": 25, "city": "Los Angeles", "marks": 90}  # Re-initializing the dictionary

print("Re-initialized Dictionary:", dictionary)

print("Iterating through the dictionary:")

for key, value in dictionary.items():  # Iterating through key-value pairs
    print(f"{key}: {value}")  # Printing each key-value pair

print("End of dictionary operations.")  

print("Final Dictionary:", dictionary)  # Displaying the final state of the dictionary

print("Total number of items in the dictionary:", len(dictionary))  # Getting the number of items in the dictionary

print("End of program.")  # Indicating the end of the program

# End of dictionary operations

dictionaryArray = [{"name": "John", "age": 30, "city": "New York", "marks": 85},
                   {"name": "Alice", "age": 25, "city": "Los Angeles", "marks": 90},
                   {"name": "Bob", "age": 22, "city": "Chicago", "marks": 78}]

print("Array of Dictionaries:", dictionaryArray)  # Displaying the array of dictionaries

for index, item in enumerate(dictionaryArray):  # Iterating through the array of dictionaries
    print(f"Dictionary {index}: {item}")  # Printing each dictionary


print("End of array operations.")  # Indicating the end of array operations

print("Total number of dictionaries in the array:", len(dictionaryArray))  # Getting the number of dictionaries in the array

print("End of program.")  # Indicating the end of the program

# End of dictionary and array operations
print("Program completed successfully.")  # Indicating successful completion of the program

# End of dictionary operations
