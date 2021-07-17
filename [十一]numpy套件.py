#numpy套件
#匯入套件
#numpy執行數度

import time 
import numpy as np:
    def calculator():
    a=np.random.rand(1000000)
    b=list(a)
    start_time=time.time()
    for_in range()

#
#ndarray產生
#可以轉換一維或多維陣列


#匯入套件
import numpy as np

#數組(tuple)轉成ndarray
X=np.array(([1,2,3],[4,5,6,]))
print(X)

#串列(list)轉換成ndarray
Y=np.array([(1,2,3),(4,5,6)])
print(Y)


import numpy as np
data1=[1,2,3,4,5]
array1=np.array(data1)
print(array1)

import numpy as a
d=[1,2,3,4,5]
a=a.array(data1)
print(a)

import numpy as np
data2=[[1,2,3,4,5],[6,7,8,9,10]]
array2=np.array(data2)
print(array2)


#匯入套件
import numpy as np
#設定資料參數

data=[1,2,3,4,5]

#將來源資料轉換成ndarray

array1=np.array(data)

array2=np.array(data,dtype=float) #小數點數值
array3=np.array(data,dtype=bool) #ture or false

print(array1)
print(array2)
print(array3)


#建立ndarray的函式
#匯入套件
import numpy as np

#可以設定列與欄
print(np.zeros((3,5)))
print()

#可以設定列與欄
print(np.ones((3,2)))
print()

#3到20中間間隔2
#包前不包後
print(np.arange(3,20,2))
print()


#0~100分成21等份
print(np.linspace(0,100,21))
print()



#建立ndarray的函式
#匯入套件
import numpy as np

print(np.zeros((3,4,)))
print()

print(np.ones((3,5)))
print()

print(np.arange(1,20,1))
print()
print(np.arange(1,1000,2))
print()

print(np.linspace(0,100,100))
print()

#ndarray陣列屬性
#匯入套件

import numpy as np
#定義資料
a = np.array([[3,6,9],[2,4,6]])
#顯示ndarray有幾維
print(a.ndim)
#用tuple顯示ndarray的形狀
print(a.shape)

print(type(a))
print(a.dtype)
print(a.data)
print(a.T)
print(a.size)
print(a.itemsize)
print(a.nbyte)


#numpy 數學＆建立方法
import numpy as np 

x=np.random.randn(5, 4)#建立一個5 * 4 的隨機資料
print(X)
print(X.mean())#取平均值
print(X.sum())#取總合
print(X.min())#取最小值
print(X.max())#取最大值
x=np.array([[2,3,4],[5,6,7]])
print(X.cumsum())

array([2,5,9,14,20,27],dtype=int32)
np.std(X)



#numpy索引
a=[i for i in range(1,6)]
b=[i for i in range(6,12)]
x=[a,b]
print(x)
y=x[1][1:]#":"這個代表後面全部
print(y)
y[1]=200
print(y)
print(x)


import numpy as np
x=np.arange(12).reshape(2,6)
print(x)
y=x[1][1:]
print(y)
y[1]=200
print(y)
print(x)

import numpy as np 
x=np.arange(12).reshape(3,4)
print(x)
y=x[[0,1,2],[2,1,0]]
print(y)

import numpy as np 
x=np.arange(12).reshape(3,4)
z=x[np.ix_([0,2],[1,3])]
print(z)

#numpy的切割
import numpy as np 
arr = np.arange(10)
slice=arr[5:8]
arr[5:8]=7
slice[1]=87
print(slice)

print(arr)







