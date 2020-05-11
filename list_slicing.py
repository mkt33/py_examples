a = [10, 21, 32, 43,54, 65, 76, 87, 98]
print("Array a[]:",a)
print()
print("Length of list:",len(a))
print("First and Third elements:",a[0],"and",a[2])
print("Last element:",a[len(a)-1], "OR",a[-1])
print("First 3 elements:",a[:3], "OR", a[0:3])
print("Last 3 elements:",a[len(a)-3:])
print("Last 3 elements:",a[-3:10])
print("All elements:",a[:], "OR",a)

#last 3 elements
print("from last to  4th elements a[:3:-1]: ", a[:3:-1])
print("from 9th to  2nd elements a[9:1:-1]: ", a[9:1:-1])

print("Array slicing a[3:-1]: ", a[3:-1])
print("a[]-slicing",a[4:len(a)])
print("a[::-1],a[::-2]",a[::-1],a[::-2])
print("Reversing elements:",a[::-1])
print("printing half elements:",a[::2]) # alternative jumps from start to end
print("printing half elements reverse order:",a[::-2]) #alternative jumps from end to start

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits[2:4:1])