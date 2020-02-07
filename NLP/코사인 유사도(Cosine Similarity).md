# 코사인 유사도(Cosine Similarity)
단어를 수취화 한 것에 대해 코사인 유사도를 이용하여 문서의 유사도를 구하는게 가능함

## 1. 코사인 유사도(Cosine Similarity)
코사인 유사도는 두 벡터 간의 코사인 각도를 이용하여 구할 수 있는 두 벡터의 유사도를 의미한다.
- 두 벡터의 방향이 같은 경우: 1
- 90°의 각을 이루는 경우: 0
- 180°로 반대 방향인 경우: -1

즉, 코사인 유사도는 -1 이상 1 이하이며, 1에 가까울수록 유사도가 높다고 할 수 있다.  
두 벡터 A, B에 대한 코사인 유사도는 다음 식과 같이 표현한다.  
<img src="https://latex.codecogs.com/svg.latex?\;similarity=cos(\theta)=\frac{A\cdot{B}}{||A||||B||}=\frac{\sum_{i=1}^{n}{A_i\times{B_i}}}{\sqrt{\sum_{i=1}^{n}{(A_i)^2}}\times{\sqrt{\sum_{i=1}^{n}{(B_i)^2}}}}" title="cosine similarity" />  

### 문서 단어 행렬에 대한 코사인 유사도
문서 단어 행렬이나 TF-IDF 행렬을 통해 문서의 유사도를 구하는 경우에는 문서 단어 행렬이나 TF-IDF 행렬이 각각의 특징 벡터 A, B가 된다.  

ex)  
문서1: 저는 사과 좋아요  
문서2: 저는 바나나 좋아요  
문서3: 저는 바나나 좋아요 저는 바나나 좋아요  

위의 문서들에 대해 단어행렬을 만들면 다음과 같다.

|-|바나나|사과|저는|좋아요|
|----|----|----|----|----|
|문서1|0|1|1|1|
|문서2|1|0|1|1|
|문서3|2|0|2|2|

### Numpy를 이용하여 코사인 유사도 계산하기
우선 코사인 유사도를 계산하는 함수를 만든다.
```python
from numpy import dot
from numpy.linalg import norm
def cos_sim(A,B):
    return dot(A,B)/(norm(A)*norm(B))
```
위의 문서들에 대한 BoW를 만든다.
```python
doc1 = np.array([0,1,1,1])
doc2 = np.array([1,0,1,1])
doc3 = np.array([2,0,2,2])
```
각 문서에 대한 코사인 유사도를 계산한다.
```python
print(cos_sim(doc1,doc2))
print(cos_sim(doc1,doc3))
print(cos_sim(doc2,doc3))
```
```
0.67
0.67
1.00
```
- 문서2와 문서3의 코사인 유사도가 1이 나옴  
-> 한 문서 내의 모든 단어의 빈도수가 똑같이 증가하는 경우 코사인 유사도가 1이다.  
- 문서2와 문서3의 코사인 유사도가 1이므로 문서1과 문서2의 코사인 유사도와 문서1과 문서3의 코사인 유사도는 같다.

참고: https://wikidocs.net/24603