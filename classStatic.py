# regular methods, class methods and static methods
# https://www.youtube.com/watch?v=rq8cL2XMM5M
# an example of a real world application is
# the datetime module: https://docs.python.org/3/library/datetime.html

class Emplyoee:

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

    # turn a regular method into a class method so that it takes the class as the 1st arguement
    # a classmethod decorator, which is a build-in Python function
    @classmethod
    def set_raise_amt(cls, amt):
        cls.RAISE_AMT = amt

    # classmethod can work as an alternative constructor;
    # a constructor is useful when repetition happens
    @classmethod
    def from_str(cls, emp_str):
        # parse the given string to get the values
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # staticmethod DOSE NOT take the instance nor the class as the 1st argument
    # a staticmethod decorator, which is a build-in Python function
    @staticmethod
    def is_workdate(date):
        # use the datetime module: https://docs.python.org/3/library/datetime.html
        # weekday is a method of the date class; Monday~Sun: 0~6
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True



# instance variables are unique. eg. our name, email addres, etc
emp1 = Emplyoee('Andrea', 'Huang', 8000)
emp2 = Emplyoee('P', 'A', 7000)

# use classmethod to set the RAISE_AMT
# equivalent to Emplyoee.RAISE_AMT = 1.06
Emplyoee.set_raise_amt(1.06)
print(emp1.RAISE_AMT)

# given a string for new employees and parse the string to get the values
emp3_string = 'John-Doe-5000'
first, last, pay = emp3_string.split('-')
emp3 = Emplyoee(first, last, pay)

print(emp3.fullname())
# use the class method to parse the string
emp4 = Emplyoee.from_str('Steven-Smith-4000')
print(emp4.email)

# use the static method
# use the datetime module: https://docs.python.org/3/library/datetime.html
import datetime
todate = datetime.date(2021, 6, 7)
print(Emplyoee.is_workdate(todate))
