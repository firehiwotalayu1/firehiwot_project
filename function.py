import timeimport time
OAOAOAOAOAOAOAOAOAOAOAOAimport math
OAOAOA
# 1. Function that takes a number and returns its square
def square(num):
    return num  


# 2. Function that checks if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # normalize string
OAOAOAOAOAOA    return s == s[::-1]
OAOAOA

# 3. Decorator that logs the execution time of a function
def log_execution_time(func):
OAOAOA    def wrapper(*args, kwargs):
        start = time.time()
OAOAOA        result = func(*args, **kwargs)
OAOAOA        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


# 4. Generator function that yields an infinite sequence of prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
OAOAOA    return True
OAOAOA
def prime_generator():
OAOAOA    num = 2
OAOAOA    while True:
OAOAOA        if is_prime(num):
            yield num
OAOAOA        num += 1


# -------------------
# Example usage
# -------------------

print("Square of 5:", square(5))  # 25

print("Is 'madam' a palindrome?", is_palindrome("madam"))  # True
print("Is 'hello' a palindrome?", is_palindrome("hello"))  # False

@log_execution_time
def test_function():
    time.sleep(1)

OAOAOAtest_function()
OAOAOA
primes = prime_generator()
OAOAOAfor _ in range(10):
OAOAOA    print(next(primes), end=" ")  # first 10 prime numbers
import math

# 1. Function that takes a number and returns its square
def square(num):
    return num


# 2. Function that checks if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # normalize string
    return s == s[::-1]


# 3. Decorator that logs the execution time of a function
def log_execution_time(func):
    def wrapper(*args, kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


# 4. Generator function that yields an infinite sequence of prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# -------------------
# Example usage
# -------------------

print("Square of 5:", square(5))  # 25

print("Is 'madam' a palindrome?", is_palindrome("madam"))  # True
print("Is 'hello' a palindrome?", is_palindrome("hello"))  # False

@log_execution_time
def test_function():
    time.sleep(1)

test_function()

primes = prime_generator()
for _ in range(10):
    print(next(primes), end=" ")  # first 10 prime numbers
