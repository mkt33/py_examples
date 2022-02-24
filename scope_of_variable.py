# types/scope of variable

# global : variable that can be accessed from anywhere in the system
# local : it can accessed from the function where it is declared and its inner function. but value can not be changed from inner function.
# nonlocal: it can be accessed from the function where it is declared. value can be changed from inner function

def my_func():
	global g
	l = "local"
	nl = "non-local"
	print("g-2.0:", g)
	g = "value changed"
	print("g-2.1:", g)
	print("l-1:", l)

	def inner_func():
		nonlocal nl
		print("nl-1:", nl)
		nl = "non local - value changed "
		print("nl-2:", nl)
		l = "changed from inner func"
		print("l-2:", l)
		print("nl-3:",nl)
	inner_func()
	print("l-3:",l)
	print("nl-4:", nl)

g = "global"
print("g-1:",g)
my_func()
print("g-3:",g)
