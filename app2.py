import random
# ---------------------- Dealing with lists ----------------------
# a list takes all data types: number, string, boolean
list_num = [3, 5.5, 4, 90, 2]
list_friend = ["Shi-fu", "Mike", "Mom", "Kristen", "Mao-mao"]

# sort a list in ascending order
list_friend.sort()
print(list_friend)
list_num.sort()
print(list_num)
num_items = len(list_friend)
print(list_friend[random.randint(0, num_items - 1)] + " is my bast friend!")

# use a negative integer to count from the end; starts from -1, -2, -3, ...
index = random.randint(-num_items, -1)
print(index)
print("On a second thought, " +
      list_friend[index] + " is also my bast friend!")

# the last index in an index range is not included
print("The 2nd item to the 4th item in my list are: ")
print(list_friend[1:4])

# add a list into an existing list
list_friend.extend(list_num)
print(list_friend)

# add ONE item onto the end of an existing list
list_friend.append("Space")
list_friend.append("Space")

# insert one item onto a specific place in an existing list
list_friend.insert(3, "Earth")
print(list_friend)

# remove a certain item in an existing list
list_friend.remove(list_friend[3])
list_friend.pop(-6)
print(list_friend)

# count the number of the same value appearing in an existing list
print(list_friend.count("Space"))

# remove a specific item 1ST APPEARS in an existing list
list_friend.remove("Space")
print(list_friend)

# empty all items in an existing list
list_num.clear()
print(list_num)

# tell me the index of a specific item in an existing list
print("The index of Mao-mao is " + str(list_friend.index("Mao-mao")))

list_friend2 = list_friend
print(list_friend2)
print("\n")

# ---------------------- Tuples ----------------------
# tuple is immutable; values inside can't be changed, edited, added...
# a tuple is very much like a list. use ()
coordinates = (77, "Andrea")
print(coordinates)
# can also create a list of tuple
coordinates2 = ([3, 4], [2, 1], [0, 2])
# coordinates2.add("flower")
print(coordinates2[2])

# following is not a tuple
coordinates3 = [(3, 4), (2, 1), (0, 2)]
coordinates3[1] = 10
print(coordinates3[2])
coordinates3.append('flower')
print(coordinates3)
# 1:23:56 https://www.youtube.com/watch?v=rfscVS0vtbw
