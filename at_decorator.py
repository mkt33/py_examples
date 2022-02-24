def func_decorator(func): # 3
    print(func) #4
    def wrapper(): #6
        print("pre call process !") #7
        func()  #8
        print("post call process") #11
    return wrapper #5
    #return wrapper

@func_decorator # 2
def py_function(): #9
    print("this is function process") #10

py_function() # 1




