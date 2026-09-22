# class Car:
#     def drive(self):
#         print("Car is moving")

# p1 = Car()
# p1.drive()
# class employee():
#     company = "hp"
#     def get_salary(self):
#         return 34000

# e1 = employee()
# e2 = employee()
# print(e1.company)
# print(f"the salary of e2 is {e2.company}")

# now constructor
# class employ():
#     company = "hp"
#     location ="indore"
#     def __init__(self , id , roll , salary):
#         self.id = id
#         self.roll = roll
#         self.salary = salary
# e1 = employ(1 , "hr" , 400000)
# e2 = employ(2 , "jr" , 300000)
# e3 = employ(3 , "sre" , 340000)
# print(e1.__dict__)
# print(e2.__dict__)
# print(e3.__dict__)

# Inheritance and polymorphism
class animals():
    location  = "india"
    def __init__(self , name , age):
        self.age = age
        self.name = name

    def speak(self):
        print("animal sound .....")

    def eat(self):
        print("it is eating")

class dog(animals):       #Inherit
        def speak(self):
            print("woof.....!:-)")
d1 = dog("honny" , 12)
print(d1.__dict__)
d1.eat()
d1.speak()
