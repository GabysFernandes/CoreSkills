''' #Function definition
def add(a,b):
    sum = a + b
    return sum

#Function call
result = add(3,5)
print(result)


def average(a,b,c):
    avg = (a + b + c) / 3
    return avg
print(average(5,10,15))



def square(num):
    return num ** 2

print(square(3))

def cub (num2):
    return num2 ** 3

print(cub(5))

def isEven(number):
    if number %2 == 0:
        return True
    else:
        return False
print(isEven(10))
print(isEven(7))


def bigger(a,b):
    if a > b:
        return True
    else:
        return False
print(bigger(9,7))


def sayHello():
    print("Hello!")

sayHello()



x = 10 #global

def demo():
    x = 5 #local
    print("Inside function: ", x)

demo()
print("Outside function: ", x)


#

name = "Gabriela"
def showName(): 
    print(name)
showName()
'''

x = 50
def add(a):
    result = x + a
    print(result)

def sub(b):
    result = x - b
    print(result)

add(5)
sub(10)
print(x)

