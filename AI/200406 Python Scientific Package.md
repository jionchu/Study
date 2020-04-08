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
- 자료의 탐색이나 정리에 아주 유용하여 데이터 분석에 빠질 수 없는 필수 패키지이다.
- 원래는 R 언어에서 제공하는 데이터프레임 자료형을 파이썬에서 제공할 수 있도록 하는 목적이었으나 더 다양한 기능이 추가됨

## 3. Matplotlib
- 파이썬에서 각종 그래프나 차트 등을 그리는 시각화 기능을 제공
- Tkinter, wxPython, Qt, GTK+ 등의 다양한 그래픽 엔진을 사용할 수 있음
- MATLAB의 그래프 기능을 거의 동일하게 사용할 수 있는 pylab이라는 서브패키지를 제공함으로 MATLAB에 익숙한 사람들은 바로 Matplotlib을 사용할 수 있다.

## 4. Tkinter - GUI Programming
- GUI에 대한 표준 Python 인터페이스이며 Window 창을 생성할 수 있음
- 윈도우이름 = tkinter.Tk()를 이용하여 가장 상위 레벨의 윈도우 창을 생성할 수 있음
- 윈도우이름.mainloop()를 사용하여 윈도우이름의 윈도우 창을 윈도우가 종료될 때까지 실행시킴
- 생성 구문과 반복 구문 사이에 위젯을 생성하고 적용함
