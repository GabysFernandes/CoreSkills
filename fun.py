'''///////////////// functions//////////////////////////////////////
def show_red():
    print("STOP!!")

def show_yellow():
    print("SLOW DOWN!!")

def show_green():
    print("GO!!")

def run_light():
    show_red()
    show_yellow()
    show_green()
run_light()
'''

'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    x = float(input("Enter a value for a: "))
    y = float(input("Enter a value for b: "))

    print("Add: ",add(x,y))
    print("Sub: ",sub(x,y))
    print("Mul: ",mul(x,y))
    print("Div: ",div(x,y))
main()

/////////////////////////////////////////////////////////////////////////
'''

'''
/////////////////////////////////////////////////////////////////////////
x = (2+2)*2
y = 2 + 2 *2
print(x,y)
////////////////////////////////////////////////////////////////////////
'''

'''

number = [1,2,3]
number.append(4)
print(number)

number = [1,2,3]
number.insert(4,20)
print(number)

number = [1,2,3]
a = number.pop(1)
print(number)
print(a)

number = [3,7,1,2,4,2]
number.remove(2)
print(number)

number = [8,2,5]
number.sort(reverse=True)
print(number)
'''

'''
///////// /////////////////////////////////////////////////////////////////
student = {"name" : "JHON" , "age" : 25 , "country" : "USA"}
student["grade"] = "A"
student["age"] = 21
del student["grade"]
print(student)

for value in student.values():
    print(value)

for key in student:
    print(key)

for key, value in student.items():
    print(key, " : " , value)
'''
'''//////////////////////////////////////
numbers = {1,2,2,3}
print(numbers)


a = {1,2,3}
b = {3,4,5}
print(a.intersection(b))
print(a.difference(b))
print(a.union(b))
'''
'''//////////////////////////////////////
student = {"name" : "Gab" , "age" : 24}
print(student)

student["city"] = "Dublin"
student["age"] = 25

del student["age"]

for key, value in student.items():
    print(key, " : " , value)

'''

a = {1,2,3,5,7}
b = {3,4,8,9,6}
print(b.intersection(a))
print(b.difference(a))
print(a.union(b))