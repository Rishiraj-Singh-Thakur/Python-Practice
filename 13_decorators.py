def logger(func):
    def wrapper():
        print("Function is called")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello")

say_hello()