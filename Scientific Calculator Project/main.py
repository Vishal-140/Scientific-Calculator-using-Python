# Scientific Calculator
import math as m
def addition(a, b):
     return a+b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b

def square(a):
    return a*a
def square_root(a):
    return m.sqrt(a)

def sin(a):
    return m.sin(a)
def cos(a):
    return m.cos(a)
def tan(a):
    return m.tan(a)
def get_degrees(rad):
    return {m.degrees(rad)}
def get_rad(degrees):
    return {m.radians(degrees)}

print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Square
8. square root
9. Sin
10. Cos
11. Tan
12. Degree
13. Radian
''')
option = eval(input("What Operation Do You Want To Perform?: "))

while option <= 13:
    if option == 1:
        print("***** Addition Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter Second Number: "))
        result = addition(a, b)
        print("The Addition of {} and {} is {}".format(a, b, result))

    elif option == 2:
        print("***** Subtraction Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter Second Number: "))
        result = subtraction(a, b)
        print("The Subtraction of {} and {} is {}".format(a, b, result))

    elif option == 3:
        print("***** Multiplication Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter second Number: "))
        result = multiplication(a, b)
        print("The Multiplication of {} and {} is {}".format(a, b, result))

    elif option == 4:
        print("***** Division Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter Second Number: "))
        result = division(a, b)
        print("The Division of {} and {} is {}".format(a, b, result))

    elif option == 5:
        print("***** Power Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter Second Number: "))
        result = power(a, b)
        print("The Powerof {} and {} is {}".format(a, b, result))

    elif option == 6:
        print("***** Power Operation *****")
        a = eval(input("Enter First Number: "))
        b = eval(input("Enter Second Number: "))
        result = power(a, b)
        print("The Power of {} and {} is {}".format(a, b, result))

    elif option == 7:
        print("***** Square Operation *****")
        a = eval(input("Enter Any Number: "))
        result = square(a)
        print("The Square of {} is {}".format(a, result))

    elif option == 8:
        print("***** Square root Operation *****")
        a = eval(input("Enter Any Number: "))
        result = square_root(a)
        print("The Square root of {} is {}".format(a, result))

    elif option == 9:
        print("***** Sin Operation *****")
        a = eval(input("Enter Any Number: "))
        result = sin(a)
        print("The Sin Value of {} is {}".format(a, result))

    elif option == 10:
        print("***** Cos Operation *****")
        a = eval(input("Enter Any Number: "))
        result = cos(a)
        print("The Cos Value of {} is {}".format(a, result))

    elif option == 11:
        print("***** Tan Operation *****")
        a = eval(input("Enter Any Number: "))
        result = tan(a)
        print("The Tan Value of {} is {}".format(a, result))

    elif option == 12:
        print("***** Degree Operation *****")
        rad = float(input("Enter Any Number: "))
        print("The Degree value is:",(get_degrees(rad)))

    elif option == 13:
        print("***** Radian Operation *****")
        degrees = float(input("Enter Any Number: "))
        print("The Radian value is:",(get_rad(degrees)))

    else:
        print("Please Choose Correct Operation")

    print()
    new_option = eval(input("Do You Want To Continue Other Operations (Yes-1 or No-0): "))
    if new_option == 1:
        option = eval(input("What Operation Do You Want To Perform?: "))
    else:
        print("...THANK YOU SO MUCH...")
        break
