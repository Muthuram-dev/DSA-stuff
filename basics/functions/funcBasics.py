# DECLARING FUNCTION IN PYTHON

def greet():
    print("hello world")
def goodbye():
    print("Goodbye")

greet()
goodbye()

# FUNCTION TAKES PARAMETER THROUGH ARGUMENTS WHEN BEING CALLED BY THE FUNC CALLER

def printContent(x): #x is a parameter
    if type(x) == int:
         print(f"The entered number is {x}")
    elif type(x) == str:
         print(f"The entered string is {x}")
    else:
         print("")

# THINGS DOWN BELOW ARE CALLED FUNCTION CALLER WITH ARGUMENTS

printContent("Hello there")
printContent(69)



# MULTIPLE PARAMETERS CAN BE THERE IN A SINGLE FUNCTION HEADER AND FUNCTION CALLER

def greetWithname(name, msg):
    print(f"{msg}, {name}")

greetWithname("User", "Welcome back!")