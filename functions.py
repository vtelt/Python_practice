print("hi")

num1 = 2
num2 = 5

def do_math(num1, num2):
    res = num1*num2
    res = res/2
    res = res + num2
    return res

def do_math1(num1, num2=7):
    res = num1*num2
    res = res/2
    res = res + num2
    return res

print(do_math(4, 7))
print(do_math1(8))

import operator

print(operator.add(2,2))
print(operator.not_(True))


def other(arg1, arg2='a', arg3=None, arg4=False):
    pass #do nothing

other(2, arg4=True)
