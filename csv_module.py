# CSV Module
# https://www.youtube.com/watch?v=q5uM4VKywbA&t=461s

# in the terminal, did pip3 install pandas first
# import pandas as pd

import csv

# ================= use reader & writer methods to read and write
# csv_file is variable name for 'SFAxApproachC_Batch_laser.csv'
# open the csv_file in read mode. Another 2 modes are: "a" append and "r+" read & write mode
# with is the context manager
with open('SFAxApproachC_Batch_laser.csv', 'r') as csv_file:

    # create a csv_reader1 variable and use the reader method to read the csv_file
    # without giving the 2nd parameter, the default delimiter is ,
    # the best practice is to check what is the delimiter used in the file you try to read,
    # and pass the correct the delimiter as the 2nd parameter
    csv_reader1 = csv.reader(csv_file)
    # for row in csv_reader1:
    #     print(row)

    # open/create a new_file called 'new laser.csv' for writing
    with open('new laser.csv', 'w') as new_file:

        # without giving the 2nd parameter, the default delimiter is ,
        # csv_writer = csv.writer(new_file, delimiter='-')
        csv_writer = csv.writer(new_file)

        # to skip the fist 6 rows
        for skip in range(6):
            next(csv_reader1)

        # loop over lines in the csv_reader1
        for line in csv_reader1:
            csv_writer.writerow(line)

            # # write the 11th column to the new_file
            # csv_writer.writerow(line[11])


# ================= use DictReader & DictReader classes to read and write
# need to call again because we have already through the csv_file
# when doing the "for line in csv_reader1:" iteration
with open('SFAxApproachC_Batch_laser.csv', 'r') as csv_file:
    # if we already know which information in the field name (column) you want
    csv_reader2 = csv.DictReader(csv_file)

    # for row in csv_reader2:
    #     print(row)

    # to skip the fist 6 rows
    for skip in range(6):
        next(csv_reader2)

    # for row in csv_reader2:
    # just want the info in field name 'AVG'
    #   print(row['AVG'])

    with open('new laser2.csv', 'w') as new_file2:

        # Specify what field names from which you want your info as the header
        header_names = ['AVG', 'STD']

        # NEED to provide the field name for the DictWriter method no matter what we want to print it or not
        csv_writer2 = csv.DictWriter(
            new_file2, fieldnames=header_names, delimiter='\t')

        # puppose we want to write out the fieldnames we specified
        csv_writer2.writeheader()

        for row in csv_reader2:

            # create an empty dictionary
            new_row_as_dict = {}
            for header_name in header_names:
                new_row_as_dict[header_name] = row[header_name]
            csv_writer2.writerow(new_row_as_dict)

# ================= Other ways to read and write a file: 3:17:15
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s

text_file = open("employees.txt", "r")

# check if a file is readable
print(text_file.readable())

# read all
print(text_file.read())

# # read one line
# print(text_file.readline())

# # take all the lines inside the file and put them inside a list
# text_reader = text_file.readlines()

# for employee in text_reader:
#     print(employee)

# close the file
text_file.close()
print()

# ----------- open the file in append mode
text_file = open("employees.txt", "a")

# # append a new employee at the end of text of the last line
# test_append = text_file.write("Toby - Human Resources")

# # append a new employee in a new line
# test_append = text_file.write("\nKelly - Customer Service")

text_file.close()
print()
# ----------- open the file in write mode: WILL OVERWRITING everthing that's in that existing file
text_file = open("employees1.txt", "w")

# write a new employee in a new line
test_append = text_file.write("\nKelly - Customer Service")

text_file.close()
