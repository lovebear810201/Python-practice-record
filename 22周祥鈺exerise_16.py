import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split as tts
from sklearn import neighbors

#呼叫load_iris()函數載入花的資料集
iris = datasets.load_iris()
#建立DataFrame物件
#columns屬性指定欄位名稱
X = pd.DataFrame(iris.data,columns=iris.feature_names)
target = pd.DataFrame(iris.target,columns=["target"])
y = target["target"]
k = 50
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
#輸出準確率
print("準確率:",knn.score(X,y))
print("----------------------------------------------")

#開始訓練模型
dtree = tree.DecisionTreeClassifier(max_depth = 4)
dtree.fit(X,y)
#輸出準確率
print("準確率:",dtree.score(X,y))
#print(dtree.predict(X))



#第二題
#分割成3:2訓練資料和測試資料集(亂數為50)
#vm
k = 10
i=[]
for k in range(1,91):  


XTrain,XTest,yTrain,yTest=tts(X , y , test_size = 0.4 , random_state=50)
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(XTrain,yTrain)
print("-----------------------------------")
print("準確率:",knn.score(XTest,yTest))

