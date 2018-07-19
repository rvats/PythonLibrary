''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''
import math

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

# This function calculate percentage of x with y
def percentage(x, y):
   return x / y * 100.0

# This function calculate percentage of x with y
def power(x, y):
   return math.pow(x,y)


print("Select any operation listed below.")
print("1. Add or +")
print("2. Subtract or -")
print("3. Multiply or *")
print("4. Divide or /")
print("5. Percentage or %")
print("6. Power or ^")

# Take input from the user 
choice = input("Enter choice [(either 1 or 2 or ... or 11) or (operator sign as +, -, *, ^, /, etc)]: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1' or choice == '+':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2' or choice == '-':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3' or choice == '*':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4' or choice == '/':
    if num2==0:
        print("Division by 0 is ∞")
    else:
        print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5' or choice == '%':
    print(num1,"%",num2,"=", percentage(num1,num2))

elif choice == '6' or choice == '^':
    print(num1,"^",num2,"=", power(num1,num2))    

    
else:
   print("Invalid input")
