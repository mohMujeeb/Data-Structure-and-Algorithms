"""
    Take the age from the user and then decide accordingly
1. If age < 18,
    print -> not eligible for job
2. If age >= 18,
    print -> eligible for job
3. If age >= 55 and age <= 57 
    print -> eligible for job but retiring soon
4. If age > 57
    print -> retirement time
"""
 
#Input Age

input_age = int(input("Enter Age: "))

#Conditionals

if input_age < 18:
    print(f"Person with age {input_age} is not eligible for job")
elif input_age <= 57:
    print(f"Person with age {input_age} is eligible for job")
    
    if input_age >=55:
        print(f"Person with age {input_age} is Eligible but Retirement soon")
else:
    print("Retirement Time")
