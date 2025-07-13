# loops/main.py
list = [1, 2, 3, 4, 5]

for i in list:
    print(i)  # Output: 1, 2, 3, 4, 5 (each on a new line)


sequence = "Hello, I am Diken Shah"
for char in sequence:
    print(char)  # Output: H, e, l, l, o (each on a new line)


table = 11
for i in range(1, table):
    print("5 x",i, "=", (5*i))  # Output: 1, 2, ..., 10 (each on a new line)


# Nested loop example
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i: {i}, j: {j}")  # Output: i: 0, j: 0; i: 0, j: 1; i: 1, j: 0; i: 1, j: 1; i: 2, j: 0; i: 2, j: 1 (each on a new line)


# While loop example
count = 0
while count < 5:
    print("Count is:", count)  # Output: 0, 1, 2, 3, 4 (each on a new line)
    count += 1  # Increment count by 1 each time


while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop if user types 'exit'
    else:
        print(f"You typed: {user_input}")  # Output: User's input (each on a new line)
        continue  # Continue to the next iteration of the loop
else:
    print("This will not execute if the loop is broken.")
# The else block here executes only if the loop completes without hitting a break statement.
# If the loop is exited with a break, the else block is skipped.
# If the loop is exited normally, the else block will execute.
# This is useful for cleanup actions or final statements after the loop.
# Note: The else block is optional and can be omitted if not needed.
# The else block is executed only if the loop completes normally without a break.
# If the loop is exited with a break, the else block is skipped.
# This is useful for cleanup actions or final statements after the loop.
# Note: The else block is optional and can be omitted if not needed.
# The else block is executed only if the loop completes normally without a break.
# If the loop is exited with a break, the else block is skipped.
# This is useful for cleanup actions or final statements after the loop.                


for i in range(5):
    if i == 3:
        print("Skipping 3")  # Output: Skipping 3
        pass # Do nothing
    print(i) # Output: 0, 1, 2, 3, 4