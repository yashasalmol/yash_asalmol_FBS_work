def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Featching from catche for",args)
            return cache[args]
        print("Computing new result for",args)
        result = func(*args)
        cache[args]=result
        return result
    return wrapper
