# Python Scientific Package
데이터 분석을 위한 3종 패키지
- numpy, pandas, matplotlib

## 1. Numpy
- 과학 계산을 위한 라이브러리로서 **다차원 배열**을 처리하는데 필요한 여러 유용한 기능을 제공하고 있음
- numpy에서 배열은 동일한 타입의 값들을 가지며, 배열의 차원을 **rank**라 하고, 각 차원의 크기를 튜플로 표시하는 것을 **shape**라 한다.
- 예를 들어 행이 2이고 열이 3인 2차원 배열에서 rank는 2이고, shape는 (2,3)이다.

### The main differences with python lists
- 속도가 굉장히 빠름
- **much less space**
- every array has one and only one **dtype**

#### python의 기본 배열 연산
```python
list1 = [0,1,2,3,4,5]
list2 = [7,6,5,4,3,2]
list1 + list2
```
```
[0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2]
```

#### numpy의 배열 연산
```python
import numpy as np
x1 = np.array(list1)
x1
```
```
array([0, 1, 2, 3, 4, 5])
```
```python
x2 = np.array(list2)
x2
```
```
array([7, 6, 5, 4, 3, 2])
```
```python
x1 + x2
```
```
array([7, 7, 7, 7, 7, 7])
```

#### 2차원 배열
```python
list2d = [[0,1,2],[3,4,5],[6,7,8]]
arr2d = np.array(list2d)
arr2d
```
```
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```
```python
arr2d_f = np.array(list2d, dtype='float')
arr2d_f
```
```
array([[0., 1., 2.],
       [3., 4., 5.],
       [6., 7., 8.]])
```
```python
arr2d_f.astype('str')
arr2d_f
```
```
array([['0', '1', '2'],
       ['3', '4', '5'],
       ['6', '7', '8']], dtype='<U11'>)
```

#### 여러 타입의 배열
```python
[1,2,'3']
```
```
[1,2,3]
```
```python
np.array([1,2,'3'])
```
```
array(['1', '2', '3'], dtype='<U11')
```
```python
arr1d_obj = np.array([1,2,'3'], dtype='object')
arr1d_obj
```
```
array([1, 2, '3'], dtype=object)
```
type을 object로 선언하면 다양한 type의 값들을 한 배열로 사용할 수 있으나 이럴바엔 numpy 안쓰고 그냥 list 쓰는게 나음
```python
arr1d_obj.tolist()
```
```
[1, 2, '3']
```

#### shape
```python
arr2 = np.array(list2d, dtype='float')
arr2
```
```
array([[1., 2., 3., 4.],
       [5., 6., 7., 8.],
       [9., 10., 11., 12.]])
```
```python
arr2.shape
```
```
(3, 4)
```

#### dtype
```python
arr2.dtype
```
```
dtype('float64')
```

#### size
```python
arr2.size
```
```
12
```

#### ndim
```python
arr2.ndim
```
```
2
```

#### Transformation matrix
```python
arr2.T.shape
```
```
(4,3)
```

```python
np.matmul(arr2, arr2.T)
```
```
array([[ 30.,  70., 110.],
       [ 70., 174., 278.],
       [110., 278., 446.]])
```

#### 난수 생성
```python
np.random.randn(20,4)
```

## 2. Pandas
- 테이블 형태의 데이터를 다루는 데이터프레임(DataFrame) 자료형을 제공함
- 자료의 탐색이나 정리에 아주 유용하여 데이터 분석에 빠질 수 없는 필수 패키지
- 원래는 R 언어에서 제공하는 데이터프레임 자료형을 파이썬에서 제공할 수 있도록 하는 목적이었으나 더 다양한 기능이 추가됨

### Core componenets of pandas
1. Series
2. DataFrame

```python
import pandas as pd
```
#### Series
```python
pd.Series([1,3,5,7])
```
```
0    1
1    3
2    5
3    7
dtype: int64
```
#### 2차원 리스트
```python
pd.Series([[1,3],[5,7]])
```
```
0    [1, 3]
1    [5, 7]
dtype: object
```
⇒ 1차원으로 처리
```python
pd.DataFrame([[1,3],[5,7]])
```
```
	0	1
0	1	3
1	5	7
```
⇒ 2차원으로 처리

#### data
```python
data = {'apples':[3,2,0,1],'oranges':[0,3,7,2]}
data
```
```
{'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
```
```python
purchases = pd.DataFrame(data)
purchases
```
```
	apples	oranges
0	3	0
1	2	3
2	0	7
3	1	2
```
#### DataFrame index 설정
```python
purchases = pd.DataFrame(data, index=['June','Robert','Lily','David'])
purchases
```
```
	apples	oranges
June	3	0
Robert	2	3
Lily	0	7
David	1	2
```
#### DataFrame column 설정
```python
purchases = pd.DataFrame(data, index=['June','Robert','Lily','David'], columns=['apples','oranges'])
purchases
```
```
	apples	oranges
June	3	0
Robert	2	3
Lily	0	7
David	1	2
```
#### DataFrame
```python
df = pd.DataFrame(np.array([[1,2,3],[4,5,6]]))
df
```
```
       0	1	2
0	1	2	3
1	4	5	6
```
```python
df.shape
```
```
(2, 3)
```
```python
df.index
```
```
RangeIndex(start=0, stop=2, step=1)
```
```python
len(df.index)
```
```
2
```
#### random number pandas mapping
```python
randomN = np.random.randn(20,4)
df = pd.DataFrame(randomN, columns=['A','B','C','D'])
df
```
```
	A	       B	       C	       D
0	2.760587	1.624110	-2.516529	1.274586
1	-0.311702	-0.455893	-1.009377	-0.364848
2	-0.007316	1.856884	-0.204956	-1.379508
3	-0.574040	0.382072	-0.736508	1.802632
4	0.272913	-0.323374	-0.049457	-0.747587
5	2.124778	1.636078	-1.422295	1.180462
6	-1.178242	1.007233	0.326853	0.952899
7	1.830472	1.378352	-0.830991	-0.721766
8	-0.719196	-0.214220	0.178843	0.147407
9	-1.279908	0.482555	-0.156208	0.633532
10	1.508434	1.184345	0.616272	0.709339
11	0.071287	1.043599	0.039450	-0.106026
12	-0.153660	0.078129	0.070615	-1.858053
13	1.931836	-0.218271	-0.597017	0.778604
14	-0.567958	-1.195066	0.106341	-0.811597
15	1.790814	0.302719	0.342159	0.489090
16	0.092199	0.022904	-0.754477	-1.381415
17	-0.283944	0.436344	0.810264	0.073221
18	-0.912812	0.770695	-0.031078	-0.282954
19	-0.770733	-0.006162	-1.280062	0.488612
```
```python
df[(df.index>10) & (df.index<16)]
```
```

       A	       B      	C      	D
11	0.071287	1.043599	0.039450	-0.106026
12	-0.153660	0.078129	0.070615	-1.858053
13	1.931836	-0.218271	-0.597017	0.778604
14	-0.567958	-1.195066	0.106341	-0.811597
15	1.790814	0.302719	0.342159	0.489090
```
```python
df.columns
```
```
Index(['A', 'B', 'C', 'D'], dtype='object')
```
```python
df.describe()
```
```
       A	       B	       C	       D
count	20.000000	20.000000	20.000000	20.000000
mean	0.281191	0.489652	-0.354908	0.043832
std	1.236116	0.810104	0.795798	0.983537
min	-1.279908	-1.195066	-2.516529	-1.858053
25%	-0.610329	-0.058176	-0.773605	-0.728221
50%	-0.080488	0.409208	-0.102833	0.110314
75%	1.579029	1.078785	0.124466	0.726655
max	2.760587	1.856884	0.810264	1.802632
```

### 파일에서 데이터 읽기
#### csv
```python
df = pd.read_csv('purchases.csv')
df
```
```
Unnamed: 0	apples	oranges
0	June	3	0
1	Robert	2	3
2	Lily	0	7
3	David	1	2
```
#### json
```python
df = pd.read_json('purchases.json')
df
```
```
	apples	oranges
David	1	2
June	3	0
Lily	0	7
Robert	2	3
```
#### sqlite3
```python
import sqlite3
con = sqlite3.connect("database.db")
df = df.set_index('index')
# Converting back to CSV, JSON, or SQL
df.to_csv('new_purchases.csv')
df.to_json('new_purchases.json')
df.to_sql('new_purchases',con)
```

## 3. Matplotlib
- 파이썬에서 각종 그래프나 차트 등을 그리는 시각화 기능을 제공
- Tkinter, wxPython, Qt, GTK+ 등의 다양한 그래픽 엔진을 사용할 수 있음
- MATLAB의 그래프 기능을 거의 동일하게 사용할 수 있는 pylab이라는 서브패키지를 제공함으로 MATLAB에 익숙한 사람들은 바로 Matplotlib을 사용할 수 있다.

```python
import matplotlib.pyplot as plt
```
#### graph 그리기
```python
plt.plot([1,2,3,4])
```
```
[<matplotlib.lines.Line2D at 0x1f57adac128>]
```
![matpotlib example](https://github.com/jionchu/TIL/blob/master/AI/images/matpotlib_example.png)  

#### label 붙이기
```python
plt.ylabel('my Label')
```
```
Text(0, 0.5, 'my Label')
```
![matpotlib example](https://github.com/jionchu/TIL/blob/master/AI/images/matpotlib_label_example.png)  

## 4. Tkinter - GUI Programming
- GUI에 대한 표준 Python 인터페이스이며 Window 창을 생성할 수 있음
- 윈도우이름 = tkinter.Tk()를 이용하여 가장 상위 레벨의 윈도우 창을 생성할 수 있음
- 윈도우이름.mainloop()를 사용하여 윈도우이름의 윈도우 창을 윈도우가 종료될 때까지 실행시킴
- 생성 구문과 반복 구문 사이에 위젯을 생성하고 적용함
