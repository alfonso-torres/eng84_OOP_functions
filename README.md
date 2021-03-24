# Functions

- What is a function and why is it useful?
  
Function is a block of code which only runs when it is called. Is a block of organized, reusable code that is used to perform a single, related action. <br/>
We use functions for the reason that they provide better modularity for your application and a high degree of code reusing.
- How to create a function
  
In Python a function is defined using the key `def` keyword.
````python
# EXAMPLE OF FUNCTION
def my_function():
  print("Hello World from a function")
````
- Function structure and arguments
  
You can pass data, known as parameters, into a function. <br/>
A function also can return data as a result. <br/>
To call a function, use the function name followed by parentheses. Here is one example:
````python
def my_function():
  print("Hello World from a function")

my_function() # "Hello World from a function" is printed
````
Arguments is the information that can be passed into functions. The arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma. <br/>
Here is one example:
````python
def greetings(name):
    print("Welcome on board " +  name)
    
# Let's see how to call this function with a parameter
greetings("James") # "Welcome on board James" is printed
````
- Function best practices

Let's create an add() function to pass 2 args and adds the 2 values.
````python
def add(num1, num2):
    print(num1 + num2)

add(3, 2) # 5 is printed
````
Let's use return statement instead of the print().
````python
def subtract(num1, num2):
    return num1 - num2 # return should be the last statement
    print("This line is to subtraction and the out is ") # doesn't get return

print(subtract(4, 2)) # 2 is printed

result = subtract(4, 3) # we save the result in a variable
print(result) # 1 is printed
````

### *Use cases*
- Exercise 1:

Create a calculator to add, subtract, divide, multiply.
Display appropriate messages with the computation values as to what the outcome is from each function:
````python
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
````
- Exercise 2:

Create a greeting function by taking user input as the user name and display it with the greeting message:
````python
# We will take the name of the user in the input
name_user = input("Please insert your name: ")

# Creating a greeting function by taking user input
def greeting(name):
    print("WELCOME on board " + name + "!. Enjoy your day.")

# Call the function to display the message
greeting(name_user)
````

### *DRY*
Do not repeat yourself is a principle of software development. It could be a guideline of computer program improvement pointed at decreasing redundancy of computer program designs, 
supplanting it with reflections or utilizing information normalization to maintain a strategic distance from excess.
