# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s
# ----------------------  if statement and taking user inputs ----------------------
# sublime text don't directly support input console, so use alt+r to run this script


# Python AUTOMATICALLY convert users' input into STRING type
# so we wrap the input around with float

numA = float(input("Enter 1st number: "))
oper = input("Enter an operand string: ")
numB = float(input("Enter 2nd number: "))

if oper == "+":
    print(numA + numB)
elif oper == "-":
    print(numA - numB)
elif oper == "*":
    print(numA * numB)
elif oper == "/":
    print(numA / numB)
else:
    print("Improper entries!")

# ----------------------  While loop 2:15:00----------------------
i = 1
while i <= 10:

    print(i)
    i += 1

print("Done with the loop")
print()

pw = "giraffe"
guessPw = ""  # allocate an empty string
i = 1
print("You have 3 times to guess the password.")

while guessPw != pw:

    guessPw = input("Enter your " + str(i) + " guess: ")
    if guessPw == pw:
        print("You win!!")
        break
    if i == 3:
        print("Sorry, you are out of luck! Good by!")
        break
    print("Wrong guessing! Guess it again.")
    i += 1

# 2:32:48  https://www.youtube.com/watch?v=rfscVS0vtbw
