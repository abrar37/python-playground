# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time


def cache(func):
    cache_value = {}
    print(cache_value)
    def wraper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wraper


@cache
def sleep_func(a, b):
    time.sleep(4)
    return a + b


print(sleep_func(4, 6))
print(sleep_func(4, 6))
print(sleep_func(2, 6))
