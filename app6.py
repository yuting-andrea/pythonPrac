# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s
# ----------------- Catching errors by Try/Except block: 3:04:25
# put regular script inside the try block
# catch the possible errors after except


try:
    deno = float(input("Enter a denominator: "))
    answer = 10 / deno
    print("10/", deno, '= ', answer)
    number = int(input('Enter a number: '))
    print('The number you enter is: ', number)

except ZeroDivisionError as err:
    print(err)
except ValueError as va_err:
    print(va_err)
except NameError as name_err:
    print(name_err)

# 3:12:45