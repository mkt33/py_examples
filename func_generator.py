# generator function
# yield  = return
# next = another execution of function 

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


item = my_gen()
print(item) # prints memory address of my_gen() function
print(next(item))

print(next(item))
print(item) # this line prints memory address of my_gen() function
print(next(item))

print('------------------------------------')
# Using for loop
for item in my_gen():
    print(item)

