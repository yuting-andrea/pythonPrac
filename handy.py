# some handy command

# print out a list of all the attributes and variables of an instance
print(emp1.__dict__)

# isinstance can check if an object is an instance of a class
print(isinstance(mgr1, Emplyoee))

# issubclass can check if a class is a subclass of a parent class
# if Manager is a subclass of Employee
print(issubclass(Manager, Emplyoee))

# return all attributs and methods of the passing object
# check what functions are available in csv module
print(dir(csv))

# check the variable type: dict, list, tuple
print(type(variable_1))

# check if the variable is an integer
print(isinstance(variable_2, int))

# chekc if an user input is a number or string
variable_3 = input("Enter a number")
print(variable_3.isdigit())

# check if a variable is one of the listed type or class, or a tuple of types and/or a tuple of classes
# if return Falso, then the variable is an object
print(isinstance(variable_4, (float, int, str, list, dict, tuple)))
