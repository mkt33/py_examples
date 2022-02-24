# You can only use expressions, but not statements.
# You can only use one expression.
# You cannot declare and use local variables.

# Program to show the use of lambda functions
# #
# syntax
# -------
# name = keyword_lambda param1, param2: return code

double = lambda x: x * 2
para2 = lambda x,y: x ** y

# Output: 10
ret = double(9)
print(ret)
print(double(10))
print("3 to the power 2 = ", para2(3,2))

