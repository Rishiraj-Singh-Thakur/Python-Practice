# def logger(func):
#     def wrapper():
#         print("Function is called")
#         func()
#     return wrapper

# @logger
# def say_hello():
#     print("Hello")

# say_hello()

# def set_alarm(func):
#     def exams():
#         print( "my exams are near so")
#         func()
#     return exams
# @set_alarm
# def get_up():
#     print("i want to get up early in the morning")

# get_up()

# use decorator
def exams(func1 , func2 ,func3):
    def tt():
        print("my time table like ",end="")
        func1()
        func2()
        func3()
    return tt

def f1():
    print("first exams of english")

def f2():
    print("second of math")

def f3():
    print("third of chemistry and physics")

exams(f1,f2,f3)()
