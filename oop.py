# https://www.youtube.com/watch?v=BJ-VvGyQxho
# instance variables are unique. eg. our name, email addres, etc
# class variables are the same for each instance, so data are shared among all instances of a class


class Emplyoee:
    # uncomment the following line if want to leave the class empty for now
    # pass

    # class variables are the same for each instance, so data are shared among all instances of a class
    # ALL_CAP for constant
    RAISE_AMT = 1.04
    NUM_EMP = 0

    # initalize class attributes
    # self refers to the instance itself but not the class
    # __init__ method runs everytime when we create a new instance
    def __init__(self, first, last, pay):
        # attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # self refers to the instance itself so we don't do self b/c we want to refer to the class
        Emplyoee.NUM_EMP += 1

    # creat a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # a method to change pay
    def app_raise(self):
        self.pay = int(self.pay * self.RAISE_AMT)


print(Emplyoee.NUM_EMP)
# instance variables are unique. eg. our name, email addres, etc
emp1 = Emplyoee('Andrea', 'Huang', 8000)
emp2 = Emplyoee('P', 'A', 7000)
print(Emplyoee.NUM_EMP)


# following 2 lines function the same
print(emp1.fullname())
print(Emplyoee.fullname(emp1))

print(emp2.email)

# override the class variable for emp1
# allow any subclass to override the constant class variable
emp1.RAISE_AMT = 1.05
# print out a list of all the attributes and variables of an instance
print(emp1.__dict__)

print(Emplyoee.RAISE_AMT)
print(emp1.RAISE_AMT)
print(emp2.RAISE_AMT)
emp2.app_raise()
print(emp2.pay)
