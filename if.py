#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  IF \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
age = int(input("How old are you?")) 

if age >= 18 :
    print("You are elegible to vote!")
else: 
    print("You are not elegible to vote!")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

number = int(input("Enter a number: "))

if number % 2 == 0: 
    print("Even number")
else:
    print("Odd number")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

score = int(input("Enter your score: "))

if score >= 90:
        print("Grade: A")
elif score >= 75:
        print("Grade: B")
elif score >= 60:
        print("Grade: C")
else:
    print("Grade: Fail")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\ SWITCH  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

day = int(input("Enter a number from 1 to 7: "))

match day: 
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
    case _:
        print("Invalid day!")

