# If elif and else statements

"""
age = 32

if age > 18:
    print("You are an adult. ")
elif age < 18:
    print("You are a minor. ")
else:
    print("You are exactly 18 years old.")

"""


# Match case statements 
status_code = int(input("Enter HTTP status code: "))

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")