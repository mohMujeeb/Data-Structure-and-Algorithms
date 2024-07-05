"""
A school has following rules for grading system:

a. Below 25 - F
b. 25 to 44 - E
c. 45 to 49 - D
d. 50 to 59 - C
e. 60 to 79 - B
f. 80 to 100 - A

ask user to enter marks and print the corresponding grade.
"""

#marks input

input_marks = int(input("Enter your marks: "))

#conditionals

if input_marks < 25:
    print(f"Grades for {input_marks} marks is F")
elif input_marks <= 44:
    print(f"Grades for {input_marks} marks is E")
elif input_marks <= 49:
    print(f"Grades for {input_marks} marks is D")
elif input_marks <= 59:
    print(f"Grades for {input_marks} marks is C")
elif input_marks <= 79:
    print(f"Grades for {input_marks} marks is B")
else:
    print(f"Grades for {input_marks} marks is A")