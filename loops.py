'''
#   \\\\\\\\\\\\\\\\\\\\\\\\\\ FOR \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
for i in range(1, 11, 2):
    print(i)



for i in range(10, 0, -1):
    print(i)
    
total = 0
for i in range(1, 101):
    total += i
    print("Sum is: ",total)

    

#   \\\\\\\\\\\\\\\\\\\\\\\\\\ WHILE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
i = 1
while i < 6:
    print(i)
    i += 1 


#    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



price = 200
txt = f"The price is {price} Euros"
print(txt)
'''
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''

#\\\\\\\\\\\\\\\\\\\\\\ Multiplication Table \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
for i in range(1,11):
    print(f"5 * {i} = {5 * i}")

#\\\\\\\\\\\\\\\\\\\\\\ Multiplication Table \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
number = int(input("Type a number: "))
for i in range(1,11):
    print(f"{number} * {i} = {{number} * i}")

#\\\\\\\\\\\\\\\\\\\\\\ Square Root\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

for i in range(1,11):
    print(f"{i} * {i} = {i * i}")

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

i = 10
while i >= 1:
    print(i)
    i -= 1
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
    print("Sum is: ",total)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
password = "admin123"
entry = ""
while entry != password:
    entry = input("Enter password: ")
print("Access granted!")

'''

for i in range(1,10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)