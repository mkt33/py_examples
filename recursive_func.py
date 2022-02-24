# recursive function

def factorial(n):
	# 5x4x3x2 = 120

	if n > 1:
		return n * factorial(n-1) # 5 * 4 * 3 * 2
	else:
		return n


n = int(input("Enter number to get its factorial: "))
fa = factorial(n)
print(n , "! = ", fa , sep="")


# HW
# write a program of recursive function to get sum between 1 and given number.
# 5+4+3+2+1 = 15 