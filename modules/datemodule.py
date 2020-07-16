import datetime
from datetime import time

#current datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)

#create objects using the constructor of the datetime classs

newdate =datetime.datetime(2020,4,5)
print(newdate)

#create date object
date1 =datetime.date(2020,4,5)
print(date1)

#return the current local date.
#This is equivalent to date.fromtimestamp(time.time()).

print(date1.today())
#Return a string representing the date and time:
print(date1.today().ctime())


#formatting date objects into readable strings, strftime()
print(newdate.strftime("%B"))

