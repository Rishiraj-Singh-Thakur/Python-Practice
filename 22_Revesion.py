def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)

        return wrapper
    return decorator

@repeat(3)
def great(name):
    print(f"hello {name}")

great("world")
