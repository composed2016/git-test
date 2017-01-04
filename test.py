#/usr/bin/python3
# coding: utf-8
import time

print(time.ctime())
time_list=time.localtime()
hours=time_list[3]
print(hours)
if 5 <= int(hours) <= 12:
    print('утро')
 elif 13 <= int(hours) <= 20:
     
     print('день')
else:
   print('вечер')

