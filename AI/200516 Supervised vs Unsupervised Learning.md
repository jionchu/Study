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
