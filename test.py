#/usr/bin/python3
# coding: utf-8

import time
import os

print(time.ctime())
name = input('Введите свой логин: ' )
time_list = time.localtime()
hours = time_list[3]
if 5 < int(hours) < 12:
    print("Доброго утра,",name)
elif 12 < int(hours) < 18:
    print("Доброго деня,",name)
elif 18 < int(hours) < 22:
    print("Доброго вечера,",name)
else:
    print("Доброй ночи,",name)
print("что бы вы хотели сделать?")
print("[1] вывести информацию о системе ")
print("[2] ")
print("[3] ")
print("[4] ")
print("[5] ")
print("[9] выход ")
do = ''
while do != 9:
do = int(input("выберите пункт:" ))
if do == 1:
    print("Данные вашей системы",os.uname())
    print ("количество просессоров", os.cpu_count())
    print ("вы находитесь",os.getcwd())
    print ("вы вошли в систему под логином",os.getlogin(), os.getuid())
elif do == 2:
    print ("2")
elif do == 3:
    print ("3")
elif do == 4:
    print ("4")
elif do == 5:
    print ("5")
else:
    pass
        
        
