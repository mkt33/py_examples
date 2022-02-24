# What is function ? : Function is a block of code to perform specific task. A function runs only when it is called
# defining function
# calling function
# arguments/parameter 
# default parameter
# No parameter function
# return value
# No return value
# dummy function
# scope of variable
# recursive function
# inner function----> check decorator
# list,tuple,dict as parameters
# @decorator

# generator
# lambda function
"""
-----------------------------------
syntax

def  function_name(parameters):
	code
	code
"""
def msg():
	print("welome to python user defined function.")

def add(a,b):
	print(a, "+" , b, "=", a+b)

def subtract(a, b=0): # b = 0 is default value of param b.
	print(a, "-", b, "=" , a-b)

def mul(a,b):
	return a*b

def dummy_func():
	pass


x = int(input("Enter any number:"))
y = int(input("Enter another number:"))

add(x,y) # calling function add()
add(30,40)
print("--subtract--")
subtract(x)
subtract(x,y)
msg()

ret = mul(x,y)
print(x, "x", y, "=", ret)

dummy_func()

# CW
# write a function that accepts two values and returns remaining value after dividing first value by second value.
