'''
LEGB
Local, Enclosing, Global, Built-In
'''

x = 'global x'

import builtins

# print(dir(builtins))
# built in functions such as min, max, etc


def test():
    global x  # hardly used
    x = 'local x'
    # print(y)
    print(x)


def test2(z):
    x = 'local x'
    print(z)


#test2('local z')


def outer():
    x = 'outer x'  # enclosing scope X variable

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
