def func_decorator(func):
    def wrapper():
        print("pre call process !")
        func()
        print("post call process")
    return wrapper() #---------------------------<<<
    #return wrapper

#@func_decorator #---------------------------------<<<
def py_function():
    print("this is function process")

#py_function() #-----------------------------------<<<

py_function = func_decorator(py_function) #------------<<<

