# Decotators
def smart_division(func):
    def innterFunction(a, b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return innterFunction

@smart_division
def division(a, b):
    return a / b

print(f"Division: {division(10,5)}")
print(f"Division: {division(5,10)}")


# Another usecase 
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(3, 4)


# Write a decorate method to track function execution time
import time

def track_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result
    return wrapper

@track_time
def slow_function():
    time.sleep(2)
    return "Done!"

slow_function()