# Bag of Words(BoW)
단어의 등장 순서를 고려하지 않는 빈도수 기반 단어 표현 방법

## 1. Bag of Words
단어의 순서는 고려하지 않고 단어의 출현 빈도(frequency)에만 집중하는 텍스트 데이터 수치화 표현 방법  
단어들이 가방 속에 넣고 섞은 후의 모습을 상상하면 된다.  

### 만드는 과정
1. 각 단어에 고유한 정수 인덱스를 부여
2. 각 인덱스의 위치에 단어 토큰의 등장 횟수를 기록한 벡터 생성

ex)  
문서1: 정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.  

문서1에 대한 BoW 만들기  
입력된 문서에 대하여 단어 집합(vocaburary)을 만들어 인덱스를 할당하고 BoW를 만든다.
```python
from konlpy.tag import Okt
import re
okt = Okt()

# 정규 표현식을 통해 온점 제거
token = re.sub("(\.)","","정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.")
# OKT 형태소 분석기를 통해 토큰화 작업 수행 -> token에 넣기
token = okt.morphs(token)

word2index = {}
bow = []
for voca in token:
    # token을 읽으면서 word2index에 없는 단어는 새로 추가한다.
    if voca not in word2index.keys():
        word2index[voca] = len(word2index)
        # 새로 들어온 단어의 bow 값을 1로 넣어준다. 단어는 최소 1개 이상이기 때문
        bow.insert(len(word2index)-1,1)
    # 이미 word2index에 있는 단어의 경우 bow 값을 1 증가
    else:
        index = word2index.get(voca)
        bow[index] = bow[index]+1
```
문서1의 각 단어에 대해 인덱스를 부여한 결과
```python
print(word2index)
```
```
{'정부': 0, '가': 1, '발표': 2, '하는': 3, '물가상승률': 4, '과': 5, '소비자': 6, '느끼는': 7, '은': 8, '다르다': 9}
```
문서1의 BoW
```python
bow
```
```
[1, 2, 1, 1, 2, 1, 1, 1, 1, 1]
```
원한다면 한국어에서 불용어에 해당되는 조사들도 제거하여 더 정제된 BoW를 만들 수도 있다.
