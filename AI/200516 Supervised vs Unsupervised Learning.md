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
