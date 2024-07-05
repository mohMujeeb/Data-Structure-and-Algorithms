#write a program that takes an input of age and prints if you
#adult are not!

#lets ask for input
input_age = int(input("Enter your age: "))

#conditionals
adult_age = 18

if input_age >= adult_age:
    print(f"The Person with {input_age} is Adult")
else:
    print(f"The Person with {input_age} is not Adult")