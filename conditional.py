number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest.")
elif b >= a and b >= c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
else:
    print("Adult")
a = float(input("Enter side 1 length: "))
b = float(input("Enter side 2 length: "))
c = float(input("Enter side 3 length: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

