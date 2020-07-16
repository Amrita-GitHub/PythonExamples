import time

#tim elapsed from 1st Jan 1970
ticks = time.time()
print(ticks)

#returns time in a time_tuple as struttime
localtime  = time.localtime(time.time())
print(localtime)

#return the formatted time
localtime1  = time.asctime(time.localtime(time.time()))
print(localtime1)