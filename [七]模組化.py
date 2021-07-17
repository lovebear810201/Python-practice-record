#模組與套件

import calendar
print(calendar.month(2021,4))

import calendar as c 
print(c.month(2021,4))

from calendar import month 
print(month(2021,5))

from calendar import month as m
print(m(2021,4)) 