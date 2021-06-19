# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s
# ------------- use For loop to loop through a collection: 2:32:45

for letter in "Giraffe":
    print(letter)
print()

friends = ['Andrea', 'Mon', 'Mike']
for name in friends:
    print(name)
print()

# i = 0:4
for i in range(4):
    print(i)
print()

# i = 1:4
for i in range(1, 5):
    print(i)
print()

for index in range(len(friends)):
    print(friends[index])
print()

for i in range(3):
    if i == 0:
        print('1st iteration')
    elif i == 1:
        print('2nd iteration')
    else:
        print('last iteration')
print()

# ----------- use For loop inside a exponential function
# 2^3
print('2^3 = ', 2**3)


def exp(base, power):
    result = 1

    for i in range(power):
        result = result * base

    return print(result)


exp(3, 0)
print()
# -------------- 2D Lists & Nested Loops: 2:47:20

# create a 2D list (grid) composes of 4 row 4 column
# no_gride = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
no_gride = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

# use index to retrive the element
print('The element in the 2nd row and the 3rd column is:',  no_gride[1][2])
print()

# use a nested for loop to print out all the ele
for row in no_gride:
    for col in row:
        print(col)
print()

# -------------- use For loop to swap letters: 2:52:50
# swap vowels of a phrase for g


def exchange(phrase):
    translation = ''
    for letter in phrase:
        if letter in 'AEIOUaeiou':
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print('After replacing the vowels in a phrase for g, the phrase "A Time Machine" becomes:',
      exchange('A Time Machine'))
