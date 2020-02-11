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
위의 문서들에 대한 [BoW](https://github.com/jionchu/TIL/blob/master/NLP/Bag%20of%20Words(BoW).md)를 만든다.
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

## 2. 유사도를 이용한 추천 시스템 구현하기
캐글에서 사용되었던 영화 데이터셋을 가지고 영화 추천 시스템을 만든다. TF-IDF와 코사인 유사도만으로 영화의 줄거리에 기반해서 영화를 추천하는 추천 시스템을 만들 수 있다.  
데이터 다운로드 링크 : https://www.kaggle.com/rounakbanik/the-movies-dataset  
위 링크의 movies_metadata.csv 파일 이용  

우선 다운로드 받은 훈련 데이터에서 2개의 샘플만 출력하여 데이터가 어떤 형식을 갖고 있는지 확인한다. csv 파일을 읽기 위해 파이썬 라이브러리인 Pandas를 사용한다.  
```python
import pandas as pd
data = pd.read_csv(r'C:\Users\USER\Desktop\movies_metadata.csv',low_memory=False)
print(data.head(2))
```
```
   adult  ... vote_count
0  False  ...     5415.0
1  False  ...     2413.0

[2 rows x 24 columns]
```
훈련 데이터는 총 24개의 열을 가지고 있고, 이 중 코사인 유사도에 사용할 데이터는 영화 제목에 해당하는 title과 줄거리에 해당하는 overview이다. 좋아하는 영화를 입력하면, 해당 영화와 줄거리가 유사한 영화를 찾아서 추천하는 시스템을 만든다.  

훈련 데이터의 양을 줄이고 학습을 진행하고자 한다면 다음과 같이 데이터를 줄여서 재저장할 수 있다.  
```python
data = data.head(20000)
```
tf-idf를 할 때 데이터에 Null 값이 들어있으면 에러가 발생하므로 tf-idf의 대상이 되는 data의 overview 열에 Null 값이 있는지 확인한다.
```python
print(data['overview'].isnull().sum())
```
```
135
```
135개의 샘플에 Null 값이 있다. pandas를 이용하면 Null 값을 처리하는 도구인 fillna()를 사용할 수 있다. 괄호 안에 Null 대신 넣고자하는 값을 넣으면 된다. 다음과 같은 경우에는 빈 값(empty value)으로 대체하여 Null 값을 제거한다.  

```python
data['overview'] = data['overview'].fillna('')
```
Null 값을 제거한 후 다시 .isnull().sum()을 수행하면 0이 나온다. 이제 tf-idf를 수행한다.  

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])

print(tfidf_matrix.shape)
```
```
(20000, 47487)
```
overview에 대하여 tf-idf를 수행한 결과 20000개의 영화를 표현하기 위해 총 47487개의 단어가 사용되었다. 이제 코사인 유사도를 사용하면 바로 문서의 유사도를 구할 수 있다.  

코사인 유사도를 구한다.
```python
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
```
영화의 타이틀과 인덱스를 가진 테이블을 만든다. 영화의 타이틀을 입력하면 인덱스를 리턴하기 위한 테이블  
```python
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print(indices.head())
```
```
title
Toy Story                      0
Jumanji                        1
Grumpier Old Men               2
Waiting to Exhale              3
Father of the Bride Part II    4
dtype: int64
```
타이틀 입력 시 인덱스 리턴 예시
```python
idx = indices['Father of the Bride Par II']
print(idx)
```
```
4
```
선택한 영화에 대해 코사인 유사도를 이용하여 가장 overview가 유사한 10개의영화를 찾아내는 함수를 만든다.  
```python
def get_recommendations(title, cosine_sim=cosine_sim):
    # 영화 타이틀에 해당하는 인덱스를 받아온다.
    idx = indices[title]
    # 모든 영화에 대해 해당 영화와 유사도를 구한다.
    sim_scores = list(enumerate(cosine_sim[idx]))
    # 유사도에 따라 영화들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # 가장 유사한 10개의 영화를 받아온다.
    sim_scores = sim_scores[1:11]
    # 가장 유사한 10개의 영화 인덱스
    movie_indices = [i[0] for i in sim_scores]
    # 가장 유사한 10개의 영화 제목
    return data['title'].iloc[movie_indices]
```
위에서 정의한 함수를 이용하여 영화 다크나이트 라이즈와 줄거리가 유사한 영화들을 찾아보자.
```python
print(get_recommendations('The Dark Knight Rises'))
```
```
12481                            The Dark Knight
150                               Batman Forever
1328                              Batman Returns
15511                 Batman: Under the Red Hood
585                                       Batman
9230          Batman Beyond: Return of the Joker
18035                           Batman: Year One
19792    Batman: The Dark Knight Returns, Part 1
3095                Batman: Mask of the Phantasm
10122                              Batman Begins
Name: title, dtype: object
```
줄거리가 유사한 영화들이 출력된다. 가장 유사한 영화는 다크 나이트이고, 그 외의 영화들도 배트맨 영화인 것을 확인할 수 있다.  