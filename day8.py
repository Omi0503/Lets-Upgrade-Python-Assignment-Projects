#Ass1 Day8

import collections
import functools


def memoize(function):
    cache = {}

    @functools.wraps(function)
    def wrap(*args, **kwargs):
        if not isinstance(args, collections.Hashable):
            return function(*args, **kwargs)

        if args in cache:
            print('returning fib({}) from cache.'.format(*args))
            return cache[args]

        print('calling fib({})'.format(*args))
        value = function(*args, **kwargs)

        print('adding fib({}) to cache'.format(*args))
        cache[args] = value

        return value

    return wrap


@memoize
def fib(n):
    """
    Returns the n'th Fibonacci number where n is an integer >= 0
    :param n: integer >= 0
    :return: n'th Fibonacci number
    """
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


for i in range(20):
    print(fib(i), end='\n\n')


#Ass2 Day8

def arm(a,b):
    for i in range(a,b):
        sum=0
        temp=i
        while temp>0:
            digit=temp%10
            sum+=digit**3
            temp//=10
        if i==sum:
            yield i

arm_no=list(arm(1,1000))
print("Armstrong numbers between 1 and 1000:",arm_no)

