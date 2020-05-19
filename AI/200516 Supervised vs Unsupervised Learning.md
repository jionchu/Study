# Supervised vs Unsupervised Learning

## 1. Scikit-learn Package

### 1) iris 데이터 읽어 들이기
- iris 데이터는 붓꽃의 데이터를 머신러닝 학습용으로 잘 정리해놓은 테스트 데이터 셋으로 꽃잎(Petal)의 크기와 꽃받침(Sepal))의 크기에 따라 iris 꽃의 종류를 분리해놓음
- 이 iris 데이터는 sklearn 라이브러리 안에 샘플 데이터로 제공됨
- 이 데이터셋에는 세 가지 붓꽃을 종류별로 50장, 총 150장의 데이터를 샘플로 제공함

```python
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
labels = pd.DataFrame(iris.target)
labels.columns = ['labels'] #y
data = pd.DataFrame(iris.data) #X
data.columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
data = pd.concat([data, labels], axis=1)
data.head()
```
![iris head](https://github.com/jionchu/TIL/blob/master/AI/images/iris_head.PNG)  
```python
data.tail()
```
![iris tail](https://github.com/jionchu/TIL/blob/master/AI/images/iris_tail.PNG)  

## 2. Supervised Learning
### 1) iris 데이터 분류하기
```python
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

# importing the necessary packages
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# downloading the iris dataset, splitting it into train set and validation set
iris = datasets.load_iris()
class_names = iris.target_names
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target']=iris.target
```
```python
# https://medium.com/dataseries/lets-build-your-first-naive-bayes-classifier-with-python-d31a5140e4bc
X_train, X_test, y_train, y_test = train_test_split(iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']], iris_df['target'], random_state=0)
NB = GaussianNB()
NB.fit(X_train, y_train)
y_predict = NB.predict(X_test)
print("Accuracy NB: {:.2f}".format(NB.score(X_test, y_test)))
```
```
Accuracy NB: 1.00
```

### 2) Bayes' theorem
![bayes theorem](https://github.com/jionchu/TIL/blob/master/AI/images/bayes_theorem.PNG)  
- 두 확률 변수의 사전 확률과 사후 확률 사이의 관계를 나타내는 정리
- 베이즈 확률론 해석에 따르면 베이즈 정리는 사전확률로부터 사후확률을 구할 수 있음

## 3. Unsupervised Learning
### 1) K-means Clustering
- random하게 중심정 k개를 잡음
- random한 포인트에서 가장 가까운 점들을 euclidian distance 구해서 가까운 것들끼리 묶음
- 새로운 그룹들의 새로운 중심점 구함
- 이 과정을 반복

label이 정해져 있지 않고 그냥 비슷한 것들끼리 묶음

k의 개수, 초기점이 중요함

### 2) iris 데이터 분류
```python
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()

labels = pd.DataFrame(iris.target)
labels.columns=['labels']
data = pd.DataFrame(iris.data)
data.columns=['Sepal length','Sepal width','Petal length','Petal width']
data = pd.concat([data,labels],axis=1)
feature = data[ ['Sepal length','Sepal width']]
feature.head()
```
```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# create model and prediction
model = KMeans(n_clusters=3, algorithm='auto') # k가 3인 model
```
#### algorithm : {"auto","full","elkan"}, default="auto"
- K-means algorithm to use
- "full" : The classical EM-style algorithm
- "elkan"
  - more efficient on data with well-defined clusters, by using the triangle inequality
  - 이전 반복에서의 모든 거리정보를 보관하여 불필요한 거리계산을 줄임
  - 대규모 데이터에서는 추가적인 저장공간을 써서 성능이 저하됨 (n_samples, n_clusters)
- "auto" chooses "elkan"
```python
model.fit(feature) # compute k-means clustering
predict = pd.DataFrame(model.predict(feature)) # predict the closest cluster each sample in X belongs to
predict.columns=['predict']
```
- model.fit(학습데이터)를 실행하면 학습 데이터를 이용하여 클러스터링을 위한 학습을 시작. 학습 데이터에 맞는 중심점 3개를 추출함
- 학습된 모델을 가지고 model.predict(데이터)를 수행하면 데이터를 학습된 모델에 맞춰서 다시 grouping하여 어느 클러스터로 grouping 되었는지 라벨 리턴
- 클러스터의 라벨은 자동으로 0,1,2로 지정됨. 이 순서는 학습할 때마다 임의로 변경될 수 있음


```python
# concatenate labels to df as a new column
r = pd.concat([feature,predict],axis=1)
# print(r)
```
- 클러스터링된 라벨과 Sepal length, Sepal width를 하나의 데이터 프레인 r에 저장해서 출력

```python
centers = pd.DataFrame(model.cluster_centers_,columns=['Sepal length','Sepal width'])
center_x = centers['Sepal length']
center_y = centers['Sepal width']
# scatter plot
plt.scatter(r['Sepal length'],r['Sepal width'],c=r['predict'],alpha=0.5)
plt.scatter(center_x,center_y,s=50,marker='D',c='r')
plt.show()
```
https://bcho.tistory.com/1203
