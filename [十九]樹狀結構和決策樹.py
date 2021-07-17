





#匯入套件
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split as tts

#呼叫load_iris()函數載入花的資料集
iris = datasets.load_iris()
#建立DataFrame物件
#columns屬性指定欄位名稱
#
X = pd.DataFrame(iris.data,columns=iris.feature_names)
target = pd.DataFrame(iris.target,columns=["target"])
y = target["target"]
#分割成67%訓練資料集和33%測試資料集
XTrain,XTest,yTrain,yTest=tts(X , y , test_size = 0.33 , random_state=1)
#開始訓練模型
dtree = tree.DecisionTreeClassifier(max_depth = 4)
dtree.fit(XTrain,yTrain)
#輸出準確率
print("準確率:",dtree.score(XTest,yTest))
print(dtree.predict(XTest))
print(yTest.values)



#鄰近演算法
#匯入套件
import pandas as pd
import numpy as np
from sklearn import neighbors
#建立訓練資料 X,y
X = pd.DataFrame({
    "抗酸性":[7,7,3,1],
    "紙張強度":[7,4,4,4]})
y = np.array([0,0,1,1])
#設定變數K
k = 4

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
#預設新產品[3,7]的分類1:好0:壞
new_tissue=pd.DataFrame(np.array([[3,7]]))
pred = knn.predict(new_tissue)
print(pred)



#鄰近演算法
#匯入套件
import pandas as pd
import numpy as np
from sklearn import neighbors
#建立訓練資料 X,y
X = pd.DataFrame({
    "抗酸性":[7,7,3,1,1],
    "紙張強度":[7,4,4,4,1]})
y = np.array([0,0,1,1])
#設定變數K
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
#預設新產品[3,7]的分類1:好0:壞
new_tissue=pd.DataFrame(np.array([[3,7]]))
pred = knn.predict(new_tissue)
print(pred)