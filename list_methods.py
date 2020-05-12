"""
copy()	Returns a copy of the list
clear()	Removes all the elements from the list
count()	Returns the number of elements with the specified value
index()	Returns the index of the first element with the specified value
reverse()	Reverses the order of the list
append()	Adds an element at the end of the list
sort()	Sorts the list
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
insert()	Adds an element at the specified position
extend()	Add the elements of a list (or any iterable), to the end of the current list

"""

fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'grape', 'apple', 'banana']
fruits0 = fruits.copy()
print("0: ",fruits0)
fruits1 = fruits #this links both variable : change in one variable reflects on another
print("0-0: ",fruits1)
fruits0.clear()
print("0-1",fruits0)
print("1:",fruits.count('apple'))
print("2:",fruits.count('peach')) #count that doesnot exist in list
print("3:",fruits.index('banana'))
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
print("4:",fruits)
fruits.append('grape')
print("5:",fruits)
fruits.sort()
print("6:",fruits)
fruits.pop()
print("7:",fruits)
fruits.remove("banana")
print("8:",fruits)
fruits.insert(1, "orange")
print("9:",fruits)
vegs = ['cucumber','carrot','radish']
#fruits.extend(vegs)
fruits.extend(['cucumber','carrot','radish'])
print("10: ",fruits)
print('11: index of carrot',fruits.index('carrot'))
print('11: 2nd index of apple:',fruits.index('apple',fruits.index("apple")+1))
fruits.insert(fruits.index('carrot'),'tomato')
print("12: Tomato added:",fruits)
for element in vegs:
	if element in fruits:
		fruits.remove(element)
print("13: ",fruits)


#some tricks
for i,v in enumerate(fruits):
	print(i,v,sep=":")




questions = ['name', 'age', 'favorite color','country','address']
answers = ['Bill', '50 year', 'blue','Nepal','Kathmandu-28']
for q, a in zip(questions, answers):
	print ('What is your {0}?  It is {1}.'.format(q, a))

for fruit in sorted(fruits):
	print(fruit)

nums = [x for x in range(0,10)]
print(nums)

