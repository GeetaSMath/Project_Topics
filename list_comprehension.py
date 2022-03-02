# LIST COMPREHENSION
numbers= []
for i in range(1,6):
    numbers.append((2**i))
print(numbers)

# using list comprehension .
numbers = [2**i for i in range(1,6)]
print(numbers)


# multiple loops in list comprehension .
val1 = ["Geeta", "Pallavi","Shweta"]
val2= ["Math", "Patile", "Wali"]
new_list = [(m, n) for m in val1 for n in val2]
print(new_list)

# DICTIONARY COMPREHENSION
# without using comprehension
old_price = {'milk':1.0, 'coffee':2.3, 'bread':2.5}
new_price=dict()
for key, value in old_price.items():
    if value > 2:
        new_price[key]=value*1.5
    else:
        new_price[key]=value
print(new_price)

# using comprehension
old_price =  {'milk':1.0, 'coffee':2.3, 'bread':2.5}
new_price = {key:value*1.5 if value>2 else value for (key,value) in old_price.items()}
print(new_price)

