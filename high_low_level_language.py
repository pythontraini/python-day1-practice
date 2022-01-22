'''n1 = 10
n2 = 20

n3 = 90
n4 =89


print(n1 + n2)
print(n1.__add__(n2))

print(n3 +                        n4)

print(n3.__add__(n4))

print("here we are trying to print list values")
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
print(my_list)


list1 =[1,2,3,4,5,6]

print(list1)'''
'''result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
    
print(result)'''
'''print("hello world")

def result(num1,num2):
    print(num1 * num2)
    return num1 * num2
	

result(10,5)


num1 = input("Enter your name  ==== ")

num2 = input("Enter your age   ===")

print(num1,num2)

print("welcome to python online sessions")
'''

# Program make a simple calculator

# This function adds two numbers
'''def add(x, y):
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


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
'''


def add(a,b):
  print(a * b)
  return a * b
    
print(add(1,2))



num1 = input("Enter a number")
print(num1)