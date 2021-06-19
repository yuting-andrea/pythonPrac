# ----------------------  Create a function 1:24:25----------------------

# function definition; name in lower case, compound_name is joined by _
# meat needs to be indented
def sayhi():
    print("Hello User!")


def sayName(name):
    print("Hello " + name)


def cube(num):
    result = num * num * num
    return print(result)


# function call
sayhi()
sayName("Andrea")
cube(5)

# ----------------------  if statement ----------------------
isMale = True
isTall = False

if isMale and isTall:
    print("Male and tall")
elif isMale and not(isTall):  # not is a logical operator
    print("Short male")
elif isMale or isTall:  # this condition also meets but the execution order is top to bottom
    print("Male or tall")
else:
    print("Neither male or tall.")

# ----------------------  if statement and comparison----------------------


def maxNum(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


print('The max number among the three is ', maxNum(-5, 4, 4))
