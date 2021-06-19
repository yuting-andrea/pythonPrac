# ----------------------  Use Dictionaries ----------------------
# a special structure that stores key-value pairs:
# a key-value pair is analogus to word-definition in a regular dictionary
# a key should be unique and is used to access the associate value

monthConversions = {
    "Jan":  "January",
    "Feb":  "February",
    "Mar":  "March",
    4:  "April",
    5:  "May",
    6:  "June"}
print(monthConversions["Mar"])
print(monthConversions.get("Mar"))
# passing a 2nd user defined string as a message when there is no matching key
print(monthConversions.get(7, 'Not a valid key!'))
print(monthConversions[6])
print()
