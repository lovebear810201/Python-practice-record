#pandas套件

#Series概述  第一個字一定要大寫

import pandas as p
s=p.Series([1,-3,5,-7])
print(s)
print('-----')#分隔線
print(s.values)
print('-----')
print(s.index)

s=p.Series([1,-3,5,-7,11,12,13,-15])
print(s)
print('-----')#分隔線
print(s.values)
print('-----')
print(s.index)

import pandas as pd
ss1=pd.Series([4,7,-5,3],index=['a','b','c','d'])
print(ss1)
print(ss1.index)
print(ss1['a'])
print('a'in ss1)
print(7 in ss1)
print(7 in ss1.values)



