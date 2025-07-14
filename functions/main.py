def calculateAverage():
    total = 0
    count = 0
    
    while True:
        try:
            number = float(input("Enter a number (or type 'done' to finish): "))
            total += number
            count += 1
        except ValueError:
            user_input = input("Type 'done' to finish or press Enter to continue: ")
            if user_input.lower() == 'done':
                break
    
    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"The average of the entered numbers is: {average}")



calculateAverage()# This function calculates the average of numbers entered by the user.
# It continues to prompt for numbers until the user types 'done'.
# It handles invalid inputs gracefully and calculates the average of valid numbers
# entered by the user.
# If no numbers are entered, it informs the user that no numbers were entered.
# If numbers are entered, it calculates and prints the average.
# This function is useful for scenarios where you want to gather user input and perform calculations based on that input.
# It can be used in various applications where user interaction is required to gather numerical data.
# The function uses a while loop to continuously prompt for input until the user decides to finish.
# It uses exception handling to manage invalid inputs and ensure the program doesn't crash.
# The average is calculated only if at least one valid number is entered.
# The function is designed to be user-friendly and robust against common input errors.


def calculateOfArea(number1, number2) -> float:
    """
    This function calculates the area of a rectangle given its length and width.
    
    :param number1: Length of the rectangle
    :param number2: Width of the rectangle
    :return: Area of the rectangle
    """
    return number1 * number2

        
area = calculateOfArea(5, 10)
print(f"The area of the rectangle is: {area}")  # Output: The area of the rectangle is: 50
# This function calculates the area of a rectangle given its length and width.
# It takes two parameters: number1 (length) and number2 (width).
# The function returns the area calculated as length * width.



def recurssionFibonacci(n):
    """
    This function calculates the nth Fibonacci number using recursion.
    
    :param n: The position in the Fibonacci sequence
    :return: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recurssionFibonacci(n - 1) + recurssionFibonacci(n - 2)
    

fiboNacci = recurssionFibonacci(10)
print(f"The 10th Fibonacci number is: {fiboNacci}")  # Output: The 10th Fibonacci number is: 55
# This function calculates the nth Fibonacci number using recursion.
# It takes one parameter n, which represents the position in the Fibonacci sequence.
# The function returns the nth Fibonacci number by recursively calling itself.
# The base cases are when n is 0 or 1, returning 0 and 1 respectively.
# For other values of n, it returns the sum of the two preceding Fibonacci numbers.
# This function is useful for understanding recursion and the Fibonacci sequence.
# It can be used in various applications where Fibonacci numbers are needed, such as in algorithms or mathematical computations.
