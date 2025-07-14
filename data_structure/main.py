marks = [56, 78, 45, 89, 67, 90, 34, 23, 67, 88]
mixed = ["Diken", 54, True, 45.6, "Python", 78]
# Lists
marks.append(100)
print("Append", marks)
# marks.extend(mixed) # Merging two lists
# print(marks)
marks.insert(0, 50) # Inserting at the beginning
print("Insert", marks)
marks.remove(34) # Removing an element
print("remove", marks)
marks.sort() # Sorting the list
print("Sort", marks)
marks.reverse() # Reversing the list
print("Reverse", marks)
marks.pop() # Removing the last element
print("pop", marks)
marks[2] = 99 # Updating an element
print("Updating", marks)
marks[0:3] = [10, 20, 30] # Slicing
print("Slicing", marks)
marks.clear() # Clearing the list   
print("Cleaning", marks)


# List comprehension
tableOfFive = [5*i for i in range(1, 11)]
print("Table of Five:", tableOfFive)

squared = [x**2 for x in range(5)]
print(squared) # Output: [0, 1, 4, 9, 16]

# -------------------------------------------------------------------------------

# Tuples 
tuple = (1, 2, 3, 4, 5, 2) # Immutable sequence - Cannot be changed
print("Tuple:", tuple)

single_element_tuple = (1,) # Single element tuple requires a comma
print("Single Element Tuple:", single_element_tuple)

# accessing tuple elements
print("First Element:", tuple[0])
print("Last Element:", tuple[-1]) # Negative indexing
print("Slice of Tuple:", tuple[1:4]) # Slicing a tuple  
# Tuple operations
print("Length of Tuple:", len(tuple)) # Length of tuple
print("Count of 2 in Tuple:", tuple.count(2)) # Count occurrences of an element
print("Index of 3 in Tuple:", tuple.index(3)) # Index of an element 

# Tuple unpacking
a, b, c, d, e, f = tuple
print("Unpacked Values:", a, b, c, d, e, f)   

# -------------------------------------------------------------------------------
# Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)

print(type(set1))  # Checking the type of set1

# Set operations
union_set = set1.union(set2)  # Union of two sets
print("Union:", union_set)
intersection_set = set1.intersection(set2)  # Intersection of two sets
print("Intersection:", intersection_set)
difference_set = set1.difference(set2)  # Difference of two sets
print("Difference:", difference_set)
symmetric_difference_set = set1.symmetric_difference(set2)  # Symmetric difference  

# Set operations
print("Symmetric Difference:", symmetric_difference_set)
set1.add(6)  # Adding an element to set1
print("Set 1 after adding 6:", set1)
set1.remove(1)  # Removing an element from set1     