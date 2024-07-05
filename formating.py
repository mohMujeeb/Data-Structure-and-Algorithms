#Formating output handling in Python 

"""Various Techniques includes:
    _ format() method
    _ f-string
    _ % operators
    _ sep and end parameters
    
"""
    
#Using format()
amount = 125.75

print("Amount is ${:.2f}".format(amount))

#Using  Sep and End Parameter

print("1", "04", "2024", sep="-")

print("Mujeeb", "Ur", "Rehman", sep=" ")

print("mujeeburr260", "gmail.com", sep="@")

#Using F-strings in Python

name = "Mujeeb"
age = 20

print(f"My Name is {name}, and I'm {age} years old")

#Using % Operators

value = int(input("Enter a value: "))

add = value + 10

print("The sum is %d" %add)