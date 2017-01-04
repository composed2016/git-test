#/usr/bin/python3
# coding: utf-8
import time

print(time.ctime())
time_list=time.ctime()
hours=int(time_list[11] + time_list[12])
print(hours)
if 5 >= hours <= 12:
    print('утро')
 elif 13 >= hours >= 20:
     print('день')
else:
   print('вечер')

