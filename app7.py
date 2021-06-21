# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s
# ------------- class & object: 3:44:00

from Student import Student

student1 = Student('Andrea', 'Aerospace Engineering', 3.8, False)
print(student1.__dict__)
print()
print(student1.name, '\'s major is ', student1.major, '.')
print('Is', student1.name, 'on probation?', student1.is_on_probation)

print(student1.is_on_honor_roll())
