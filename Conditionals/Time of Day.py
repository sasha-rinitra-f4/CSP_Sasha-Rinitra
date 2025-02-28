#Sasha Rinitra, Time of day Python

import time

current = time.time()
now = time.ctime(current)
local_time = time.localtime(current)
hour = local_time.tm_hour

if hour >= 12 and hour <= 16:
    print("Good afternoon!!")
elif hour > 16 and hour <= 19:
    print("Good Evening!!")
elif hour > 19:
    print("Good night!!")
else:
    print("Good morning!!")