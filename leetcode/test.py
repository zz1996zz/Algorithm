import functools

a=[1,2,3,4,5]
b=functools.reduce(lambda x, y: 10*x + y, a)
print(b)
functools.re