var = input("Enter: ")

while var.isnumeric() == True:
    var = input("Enter: ")
    if var.isnumeric() == True:
        print("Your Input ", var)
print("end of while loop")