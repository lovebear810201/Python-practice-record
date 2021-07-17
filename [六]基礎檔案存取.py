#第六章基礎檔案存取練習筆記
#基本輸入輸出
name = input('please enter ur name :')
print((name),'welcome:)')


#將資料輸出至檔案
t = '''將此文的內如全部都存起來
sdf
wer
werw
rr23r32r
r2332r
r2332r
r2323r
2
'''
print(t,file=open('test.txt','w'))


#寫入檔案到路徑底下
file = open('檔案名稱.txt','w')
file.write('寫入資料到檔案\n')
file.write('jtiogjo\n')
file.write('12345\n')
file.write('rogjierojgoejoe')
file.write('fffffff')
file.close()

file = open('123.txt','w')
file.write('操你媽\n')
file.write('jtiogjo\n')
file.write('12345\n')
file.write('rogjierojgoejoe')
file.write('fffffff')
file.close()

#寫入檔案到路徑底下
#亂數產生10個整數範圍1~100寫入檔案中
import random as r 
file = open('123.txt','w')
for i in range (10): #出現10個結果
    file.write(str(r.randint(1,100))+'\n') #寫入字串裡範圍是1~100
file.close()

#讀取檔案
file = open('123.txt','r')
content = file.read()
print(content)
file.close()

f = open('123.txt','r')
c = f.read()
print(c)
f.close()

#with敘述
with open('123.txt','r')as file:
    content=file.read()
    print(content)

with open('123.txt','r')as f:
    c=f.read()
    print(c)    
