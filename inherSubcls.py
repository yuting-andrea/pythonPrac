# inheritance and subclass
# https://www.youtube.com/watch?v=RSl87lqOXDE
# 

class Emplyoee:

    RAISE_AMT = 1.04

    # initalize class attributes
    # self refers to the instance itself but not the class
    # __init__ method runs everytime when we create a new instance
    def __init__(self, first, last, pay):
        # attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # creat a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # a method to change pay
    def app_raise(self):
        self.pay = int(self.pay * self.RAISE_AMT)


# create a subclass that inherites attributes & methods from the parent class
class Developer(Emplyoee):
    # override parent's attribute
    RAISE_AMT = 1.05
    # want to add a parameter in the __init__ method

    def __init__(self, first, last, pay, prog_lang):
        # inherite from the parent class
        super().__init__(first, last, pay)
        # Emplyoee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Emplyoee):
    def __init__(self, first, last, pay, emp_list=None):
        super().__init__(first, last, pay)
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove_emp(emp)

    def print_emp_list(self):
        for emp in self.emp_list:
            print('-->', emp.fullname())


dev1 = Developer('Corey', 'Schafer', 5000, 'Python')
dev2 = Developer('Test', 'Last', 7000, 'Java')
print(dev1.email)
print(dev2.prog_lang)

mgr1 = Manager('Sue', 'Smith', 9000, [dev1])
print(mgr1.fullname())
mgr1.add_emp(dev2)
# mgr1.remove_emp(dev1)
mgr1.print_emp_list()


# isinstance can check if an object is an instance of a class
print(isinstance(mgr1, Emplyoee))

# issubclass can check if a class is a subclass of a parent class
print(issubclass(Manager, Emplyoee))


# # print out Methods/Data/other attributes inherited from the parent class, Employee
# print(help(Developer))
