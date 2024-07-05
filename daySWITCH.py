#Take the day no and print the corresponding day 
#for 1 print Monday so on for 7 print Sunday

input_day = int(input("Enter a number range 1-7: "))

if input_day <= 7:
    match input_day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
            
else:
    print("Input Value is out of Range")
            
     