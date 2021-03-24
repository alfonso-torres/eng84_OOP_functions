# What is a functions
# Why functions

# How to create a function
# Syntax to create a functions: def is Python keyword that tells the interpreter that the functions is being declared

# Let's create one - Syntax -> def name_of_the_function():
# Greeting function first iteration
# def greetings():
#    print("Welcome on board ")
# if we run this program now there be no outcome as we have not called this function

# Let's see how to call this function
# greetings()

# Second Iteration to take the argument
def greetings(name):
    print("Welcome on board " +  name)

# Let's see how to call this function
greetings("James")
#my_name = "Jose"
#greetings(my_name)

# Third Iteration - Let's create an add() to pass 2 args and adds the 2 values
def add(num1, num2):
    print(num1 + num2)

add(3, 2)

# Fourth Iteration - To use return statement instead of the print()
def subtract(num1, num2):
    print("This line is before the return statement")
    return num1 - num2 # return is the end of the function so only do the code before this statement will work
    # return should be the last statement
    print("This line is to subtraction") # doesn't get return

print(subtract(4, 2))

result = subtract(4, 3)
print(result)

# Create a calculator to add, subtract, divide, multiply
# display appropriate messages with the computation values as to what the outcome is from each function
# create a greeting function by taking user input as the user name and display it with the greeting message

print("----Exercise 1----")
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

# We will make some prints to see the result of the different functions:
num1 = 4
num2 = 2

result1 = add(num1, num2)
print("The sum of the values " + str(num1) + " and " + str(num2) +  " is: " + str(result1))

result2 = subtract(num1, num2)
print("The subtraction of the values " + str(num1) + " and " + str(num2) + " is: " + str(result2))

result3 = multiply(num1, num2)
print("The multiplication of the values " + str(num1) + " and " + str(num2) + " is: "+ str(result3))

result4 = divide(num1, num2)
print("The division of the values " + str(num1) + " and " + str(num2) + " is: " + str(result4))

print("----Exercise 2----")
# We will take the name of the user in the input
name_user = input("Please insert your name: ")

# Creating a greeting function by taking user input
def greeting(name):
    print("WELCOME on board " + name + "!. Enjoy your day.")

# Call the function to desplay the message
greeting(name_user)
