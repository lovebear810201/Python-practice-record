import json 
fn = '123.json'
with open(fn) as fn0bj:
    data=json.load(fn0bj)
print(data)
print(type(data))

fn2 = '456.json'
with open(fn2) as fn0bj2:
    data2=json.load(fn0bj2)
print(data2)
print(type(data2))

#變化

import json 
f1 = '123.json'
with open(f1) as f1:
    d1=json.load(f1)
print(d1)
print(type(d1))

f2 = '456.json'
with open(f2) as f2:
    d2=json.load(f2)
print(d2)
print(type(d2))


#json檔案寫入（python資料格式儲存成json檔案）

import json 
dictobject = {'x':60,'y':55,'z':90}
fn='123456.json'
with open(fn,'w')as fn0bj:
    json.dump(dictobject,fn0bj)
listarray = [{'X':"一二三",'y':55,'z':90},{'a':10,'b':25,'c':30}]
fn='654321.json'
with open(fn,'w')as fnarray:
    json.dump(listarray,fnarray,ensure_ascii=False)


#json範例
import json
with open ("NewBike.json",encoding='utf8')as file:
    data=json.load(file)
    for item in data:
         print ([item['sno'],item['sna'],item['tot']])

