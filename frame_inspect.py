import sys


def tracer(frame, event, arg):
    locals = frame.f_locals
    if locals:
        print 'locals variables: ', locals
    return tracer


def a():
    print 'in a()'
    mystr = "mystr"
    mydict = {"mykey": "myvalue"}
    mylist = [1, 2, 3]
    return mystr * 2


sys.settrace(tracer)
a()
