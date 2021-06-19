# Datetime Module
# https://www.youtube.com/watch?v=eirjjyP2qcQ

# from datetime import time
# from datetime import datetime # <-- is different than the following line
import datetime

# ----------- datetime.date ----------- year, month, and day
# no leading 0 for month and date
d = datetime.date(2016, 4, 7)
print(d)
d_today = datetime.date.today()
print(type(d_today.day))
print(d_today.weekday())
print("The weekday of today in ISO form is",
      d_today.isoweekday(), 'bc Monday is 1')

tdelta = datetime.timedelta(days=7)
print('One week after today is', d_today + tdelta)
print('\n')

# ----------- datetime.time ----------- hours:minutes:seconds.microseconds
# no leading 0 for hour, minute, second, microsecond
t = datetime.time(9, 33, 4, 3)
print(t.microsecond)
print('\n')

# ----------- datetime.datetime ----------- year, month, day, and hours:minutes:seconds.microseconds
dt = datetime.datetime(2016, 7, 28, 12, 30, 45, 22)
print('The date is', dt.date(), 'the time is', dt.time())
print('\n')

# ----------- datetime.datetime.today -----------
# a specified format
f = '%B %d, %Y'
dt_str = dt.strftime(f)
print('Convert the Datetime 2016-07-28 12:30:45.000022 to a string that conforms with the specified format is', dt_str)
dt_num = datetime.datetime.strptime(dt_str, f)
print('Parse the string "July 28, 2016" with the specified format to Datetime is', dt_num)

