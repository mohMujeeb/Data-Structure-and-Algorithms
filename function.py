"""_
Python Function:
    A Python function is a block of organized, reusable code that 
    is used to perform a single, related action. Functions provide
    better modularity for your application and a high degree of 
    code reusing.
    
Types of the Python Function:
    -Built in Funcitons
    -Functions defined in built in modules
    -User Defined Functions
    
Built-in Python Functions:
    -print()
    -len()
    -int()
    -sum()
"""
# Python Function

def callme():
    print("Greetings")

callme()

# Function calling mechanisms:
#   -Call by Value
#   -Call by Reference

# Python uses call by reference object concept

# Immutable objects show "pass by value" whereas mutable objects show "pass by reference"


def pass_by_value(num):
    
    num = num * 2
    print("Function Value updated to : ", num)
    return

def pass_by_reference(list):
    
    list[0] = "M"
    print("Fuction List Updated to :", list)
    return

input_list = ["Mujeeb"]
input_num = 10

print("Number Before : ", input_num)
pass_by_value(input_num)
print("Number After Function Number Value :", input_num)


print("List Before : ", input_list)
pass_by_reference(input_list)
print("List After Function List Value: ", input_list)