# temperature = float(input("Type the Temperature: "))

# if temperature < 0:
  #  print("Freezing weather!")


# number = int(input("Enter a number: "))

#if number > 0: 
    #print("Positive!")
#else:
   # print("Not positive")

'''

hour = int(input("Type the time: "))

if hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")
    
'''

color = input("Type a color: ")

match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Ready!")
    case "green":
        print("Go!")
    case _:
        print("Invalid Color!!")


num = int(input("Enter a number: "))

message = "Zero" if num == 0 else "Non-zero"
print(message)