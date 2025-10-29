'''gabriela = [1,2,5]
print(gabriela[2])


gabriela = [1,2,5]
gabriela.append(6)
print(gabriela)



gabriela = [1,2,5]
gabriela.remove(1)
print(gabriela)



gabriela = [26,99,12,50,100]
gabriela.sort()
print(gabriela)



gabriela = [26,99,12,50,100]
print(len(gabriela))

number.pop(0)


number = []
for i in range(5):
    num = int(input('Type a number: '))
    number.append(num)
print(f'All numbers: {number}')

first = number[0]
number.remove(first)
print(f'Removed the first number: {number}')

number.append(6)
print(f'Added a new number: {number}')

number.sort()
print(f'Organized the numbers: {number}')
 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\TUPLE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
my_tuple = (10,20,30,40)
print(my_tuple)
print(my_tuple[0])
print(len(my_tuple))

my_tuple1 = ("apple","banana","cherry")
print("banana" in my_tuple1)
print( my_tuple1 + ("mango",))
print( my_tuple1)
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\DICT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


my_dict = {
    "name" : "Gabriela",
    "Age"  : 24,
    "City" : "Criciuma"
}
print(my_dict.items())
print(my_dict.keys())

my_dict.update({"Country" : "Brazil", "Age" : 30})
print(my_dict)

new_my_dict = my_dict.copy()
print(new_my_dict)

new_my_dict.clear()
print(new_my_dict)


a_dict = {
    "name" : "Gabriela",
    "age"  : 24,
    "grade" : "aa"
}
print(a_dict)
a_dict.update({"City" : "Criciuma"})
a_dict.update({"grade" : "AAA"})
print(a_dict)
new_dict = a_dict.copy()
new_dict.clear() 

print(new_dict)

'''

fruit_tuple = ("Banana" , "Mango" , "Orange")
print(fruit_tuple)

number_tuple = (1,2,3,4,5)
print(number_tuple[0])
print(number_tuple[4])

print(len(number_tuple))

colors = ("red", "green", "blue", "yellow")
print(colors[2])
