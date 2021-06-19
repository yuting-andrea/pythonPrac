# from math module
from math import *

# create variables: variable_name
# string, aka plain text
char_name = "Tom"
# number
char_age = "50.10"
# boolean
is_male = True # True or False

# ---------------------- String ----------------------
#  concatenate string to string
print("There once was a man named " + char_name + "," )
print("he was " + char_age + " years old. ")
char_name = "John"
print("He really liked the name " + char_name + ",")
print("but didn't like being " + char_age + ".")
print("\n")

# print out whatever after \
print("Giraffe \nAcademy: \"learning basic\simple stuff\"  ")

# variable.function to modify the variable
phrase = "Giraffe Academy"
# check if phrase is all upper cases
print(phrase.isupper())
# can also combine functions
print(phrase.upper().isupper())
print(phrase)
print(phrase.upper())
print("\n")

# index of string starts with 0
print("Want the 3rd char of Giraffe: " + phrase[2])
# find the index of a certain char
print(phrase)
print(phrase.index("Ac"))
print(phrase.replace("Gir", "gIR"))
print(phrase)

print(len(phrase))
print("\n")

# ---------------------- Number ----------------------
print((3+4.5)/2 * 3)
# get the remainder
print(10%3)
var_num1 = 5
var_num2 = -2
var_num3 = 3.7
print(round(3.6))
print(var_num3.__floor__())
print(ceil(var_num3))
print(var_num2.__abs__())
print(abs(var_num2))
print(var_num1.__pow__(3))
print(pow(var_num1, 3))
array_num = [2 , -1, 7]
print(max(array_num))
print(str(var_num1) + " is a string converted from number type")
# convert a string into an integer or a number with decimal
var_num4 = "4"
var_num5 = "2.333"
print(int(var_num4) + float(var_num5))
print("\n")

# ---------------------- Take inputs from users ----------------------
print("Let's play a mad lips game!")
age_input = input("Give me a number: ")
noun_subject = input("Give me a name: ")
verb = input("Give me a transitive verb: ")
adj = input("Give me a color: ")
noun_object = input("Give me a object: ")
print("A " + age_input + "-year old " + noun_subject + " likes to ")
print(verb + " a " + adj + " " + noun_object + "!")

