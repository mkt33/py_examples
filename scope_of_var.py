


""""
Nonlocal Variables
Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
Let's see an example of how a nonlocal variable is used in Python.
We use nonlocal keywords to create nonlocal variables.
"""

















def outer():
    x = "local"
    # declaring nonlocal variable here throws error
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
    x = 'over written by outer'
    print("outer:", x)


outer()
