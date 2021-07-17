#python開放資料處理以及分析
#選取ＣＳＶ檔案

#匯入套件
import csv
#開啟檔案
fn = '123.csv'#定義檔案變數
#讀取檔案物件建立Reader物件

with open (fn,encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
#將資料轉換成串列    
    listReport = list(csvReader)
print(listReport)


#讀取CSV檔案2
#使用索引列出特定串列內容
import csv
fn = '11.csv'
with open(fn,encoding = 'utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)
print(listReport[0][1],listReport[0][0])
print(listReport[1][1],listReport[1][2])
print(listReport[3][1],listReport[3][2])

#寫入CSV檔案
with open ('檔案名稱','w',newline='')as csvFile:
    outWriter = csv.writer(csvFile)
    
with open ('檔案名稱','w',newline=''.encodeing = 'utf8')as csvFile:
    outWriter = csv.writer(csvFile)

#匯入套件    
import csv 
fn = '12.csv'
with open (fn,'w',newline='',encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['姓名','電話','ID','費用','是否前往'])
    csvWriter.writerow(['李曉明','2964736','E44347874473','100','Ture'])
    csvWriter.writerow(['王大強','2347832','A43792379247','500','False'])
    
    
#匯入套件    
import csv 
f = '13.csv'
with open (f,'w',newline='',encoding='utf-8') as c:
    cs = csv.writer(c)
    cs.writerow(['姓名','電話','ID','費用','是否前往'])
    cs.writerow(['李曉明','2964736','E44347874473','100','Ture'])
    cs.writerow(['王大強','2347832','A43792379247','500','False'])
    
    
#匯入套件    
import csv 
f = '14.csv'
with open (f,'w',encoding='utf-8') as c:
    cs = csv.writer(c)
    cs.writerow(['姓名','電話','ID','費用','是否前往'])
    cs.writerow(['李曉明','2964736','E44347874473','100','Ture'])
    cs.writerow(['王大強','2347832','A43792379247','500','False'])

import csv 
fn = '15.csv'
with open (fn,'w',newline='') as csvFile:
    csvWriter = csv.writer(csvFile,delimiter='\t')
    csvWriter.writerow(['姓名','電話','ID','費用','是否前往'])
    csvWriter.writerow(['李曉明','2964736','E44347874473','100','Ture'])
    csvWriter.writerow(['王大強','2347832','A43792379247','500','False'])
    
#讀寫檔案
import csv 
infn='16.csv'
outfn='17.csv'
with open (infn,encoding='utf-8') as csvRFile:
    csvReader = csv.reader(csvRFile)
    listReport = list(csvReader)
with open (outfn,'w',newline='',encoding='utf-8') as csvOFile:
    csvWriter = csv.writer(csvOFile)
    for row in listReport:
        csvWriter.writerow(row)
        
        
        