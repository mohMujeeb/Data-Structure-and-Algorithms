# Data Types in Python

"""
Python data types are classes and instances are objects of these classes
Following are:
    Numeric
        =>Integer
        =>Float 
        =>Complex Number
    Boolean
    Dictionary
    Set
    Sequence Type
        List 
        Tuple
        Strings
"""

#Numeric Data Types:

#Integer:
print("\nInteger")
#Positive or negative whole number without any specified range

int_eg = 100
print("Value: ",int_eg ,", Data Type: ", type(int_eg))

#Float
print("\nFloat ")
#real number with floating point representation, specified by decimal point, character "e" or "E" used for scientific Notation


float_eg = 2.85
print("Value: ",float_eg ,", Data Type: ", type(float_eg))

#Complex Number 
print("\nComplex Number")
#is represented by a complex class, it is specified as (real part)+ (imaginary part)j

complex_eg = 8 + 9j

print("Value: ",complex_eg ,", Data Type: ", type(complex_eg))


#Sequence Data Types In Python
#It is the ordered collection of similar or different data types, allows to store multiple values in an organized and efficient fashion

#String
print("\nString")
#array of bytes representing unnicode collection, It is collection of characters put in a single, double and triple quotes

string_eg = "Poland"
string_eg1 = 'England'
string_eg2 = '''I'm a Coder'''

print("Double Quotes String: ", string_eg)
print("Single Quotes String: ", string_eg1)
print("Triple Quotes String: ", string_eg2)

#Accessing Elements of String
print("\nAccessing Elements of String")
#Indexing method is used to access individual character of string, negative indexing used to access element from back of string

access_string = "Elements"

print("Original String: ", access_string)
print("Element access using Indexing: ", access_string[0])
print("Accessing Last Element: ", access_string[-1])

#List
print("\nList")

#similar to arrays, very flexible as items do not neeed to be of same type, created using []

List = []
print("An empty list: ", List)

listString = ["I'm a coder"]
print("List containg string: ", listString)

listMultivalues = ["Python", "is", "easy"]
print("List with multiple values:", listMultivalues)

accessList = ["Python", "is", "easy"]
print("Accessing element in a list:", accessList[0])


    
