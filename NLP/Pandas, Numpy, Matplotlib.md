# Pandas, Numpy, Matplotlib
데이터 분석을 위한 필수 패키지 삼대장  
세 개의 패키지 모두 아나콘다를 설치했다면 자동으로 설치되어 있다.

## 1. Pandas
Pandas는 파이썬 데이터 처리를 위한 라이브러리이다. 파이썬을 이용한 데이터 분석과 같은 작업에서 필수  
참고: http://pandas.pydata.org/pandas-docs/stable/  

아나콘다를 설치하지 않은 경우 커맨드로 별도 설치할 수 있다.
```
pip install pandas
```
Pandas의 경우 주로 pd라는 명칭으로 임포트한다.
```python
import pandas as pd
```
Pandas는 총 세 가지의 데이터 구조를 사용한다.  
1. 시리즈(Series)
2. 데이터프레임(DataFrame)
3. 패널(Panel)

이 중 데이터프레임이 가장 많이 사용된다.

### 시리즈(Series)
1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 구조
```python
sr = pd.Series([1700, 1800, 1000, 5000], index=["피자", "치킨", "콜라", "맥주"])
print(sr)
```
```
피자    17000
치킨    18000
콜라    1000
맥주    5000
dtype: int64
```
```python
print(sr.values)
```
```
[17000 18000 1000 5000]
```
```python
print(sr.index)
```
```
Index(['피자','치킨','콜라','맥주'], dtype='object')
```

### 데이터프레임(DataFrame)
2차원 리스트를 매개변수로 전달. 2차원이므로 행방향 인덱스(index)와 열방향 인덱스(column)가 존재한다. 즉, 행과 열을 가지는 자료구조이다. 시리즈에 열(column)이 추가된 구성
```python
values = [[1,2,3],[4,5,6],[7,8,9]]
index = ['one','two','three']
columns = ['A','B','C']

df = pd.DataFrame(values, index=index, columns=colums)
print(df)
```
```
        A B C
one     1 2 3
two     4 5 6
three   7 8 9
```
```python
print(df.index)
```
```
Index(['one','two','three'], dtype='object')
```
```python
print(df.columns)
```
```
Index(['A','B','C'],dtype='object)
```
```python
print(df.values)
```
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

### 데이터프레임의 생성
데이터프레임은 리스트, 시리즈, 딕셔너리, Numpy의 ndarrays, 또 다른 데이터프레임으로 생성할 수 있다.  

#### 리스트를 통해 데이터프레임 생성하기
```python
data = [['1000','Steve',90.72],
        ['1001','James',78.09],
        ['1002','Doyeon',98.43],
        ['1003','Jane',64.19],
        ['1004','Pilwoong',81.30],
        ['1005','Tony',99.14]]
df = pd.DataFrame(data)
print(df)
```
```
    0       1           2
0   1000    Steve       90.72
1   1001    James       78.09
2   1002    Doyeon      98.43
3   1003    Jane        64.19
4   1004    Pilwoong    81.30
5   1005    Tony        99.14
```
생성된 데이터프레임에 열을 지정해줄 수 있다.
```python
df = pd.DataFrame(data, columns=['학번','이름','점수'])
print(df)
```
```
    학번    이름        점수
0   1000    Steve       90.72
1   1001    James       78.09
2   1002    Doyeon      98.43
3   1003    Jane        64.19
4   1004    Pilwoong    81.30
5   1005    Tony        99.14
```
#### 딕셔너리를 통해 데이터프레임 생성하기
```python
data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
        '이름' : [ 'Steve', 'James', 'Doyeon','Jane', 'Pilwoong', 'Tony'],
        '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)
```
```
    학번    이름        점수
0   1000    Steve       90.72
1   1001    James       78.09
2   1002    Doyeon      98.43
3   1003    Jane        64.19
4   1004    Pilwoong    81.30
5   1005    Tony        99.14
```

### 데이터프레임 조회하기
데이터프레임에서 원하는 구간만 확인하기 위한 명령어  
- df.head(n) - 앞 부분 n개만 보기
```python
print(df.head(3))
```
```
    학번    이름        점수
0   1000    Steve       90.72
1   1001    James       78.09
2   1002    Doyeon      98.43
```
- df.tail(n) - 뒷 부분 n개만 보기
```python
print(df.tail(3))
```
```
3   1003    Jane        64.19
4   1004    Pilwoong    81.30
5   1005    Tony        99.14
```
- df['열이름'] - 해당되는 열 확인
```python
print(df['학번'])
```
```
0   1000
1   1001
2   1002
3   1003
4   1004
5   1005
Name: 학번, dtype: object
```