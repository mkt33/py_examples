def func_args4(dct):
	print("4-1:",dct.popitem())
	print("4-2:",dct)
def func_args3():
	# global t
	print("3-1: ",t)
	# t = (5,6,7)	
def func_args2(lst, *arg, **kwargs):
    print("2-1:",lst)
    print("2-2:",arg)
    print("2-3:",kwargs)
def func_args1(strings, *args, **kwargs):
    print ("1-1:",strings)
    print ("1-2:",args)
    print ("1-3:",kwargs)

strings = 'pos1={1} pos2={2} pos3={3} foo={foo} bar={bar}'
func_args1(strings, 1, 2, 3)
#pos1=1 pos2=2 pos3={3} foo={foo} bar={bar}
func_args1(strings, 42, bar=123, foo='hello')
#pos1=42 pos2={2} pos3={3} foo=hello bar=123
lst = [1,2,3,4]
func_args2(lst, 11,22,33, a=11,b=22,c=33,d=44) # key:value
t=tuple(lst)
func_args3()
d={}.fromkeys(lst,"apple")
func_args4(d)
print(d)
