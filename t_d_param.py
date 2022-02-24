# tuple and dict as parameters

def formatString(stringTemplate, *args, **kwargs): # args = (42,), kwargs = {"bar":123, "foo": "hello"}
    # Replace any positional parameters
    for i in range(0, len(args)):
        tmp = '{%s}' % str(1+i)
        print(tmp)
        while True:
            # print("--------------")
            pos = stringTemplate.find(tmp)
            if pos < 0:
                break
            stringTemplate = stringTemplate[:pos] + \
                             str(args[i]) + \
                             stringTemplate[pos+len(tmp):]
 
    # Replace any named parameters
    for key, val in kwargs.items():
        tmp = '{%s}' % key 
        while True:
            pos = stringTemplate.find(tmp)
            if pos < 0:
                break
            stringTemplate = stringTemplate[:pos] + \
                             str(val) + \
                             stringTemplate[pos+len(tmp):]
 
    return stringTemplate

stringTemplate = 'pos1={1} pos2={2} pos3={3} foo={foo} bar={bar}'
print(formatString(stringTemplate, 1, 2))
#pos1=1 pos2=2 pos3={3} foo={foo} bar={bar}
print(formatString(stringTemplate, 42, bar=123, foo='hello')) # {"bar":123,"foo":"hello"}
#pos1=42 pos2={2} pos3={3} foo=hello bar=123