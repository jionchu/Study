# Supervised Learning for Document Classification

The goal of this chapter
1. How can we identify particular features of language data that are salient for classifying it?
2. How can we construct models of language that can be used to perform language processing tasks automatically?
3. What can we learn about language from these models?

### 1) Typical Steps of Supervised Classification
- Step 1: Data preparation
- Step 2: Text preprocessing
- Step 3: Feature engineering
- Step 4: Train and evaluate models

## 1. Supervised Classification

### 1) 영어 이름으로 성별 분류하기
#### ㄱ. male data와 female data 섞기
```python
import nltk
from nltk.corpus import *
from nltk.corpus import *
import random
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)
labeled_names
```
```
[('Yehudi', 'male'),
 ('Denice', 'female'),
 ('Rochette', 'female'),
 ('Isabeau', 'female'),
 ('Gerry', 'female'),
 ('Rollins', 'male'),
 ('Raphaela', 'female'),
 ('Almeria', 'female'),
 ('Cherrita', 'female'),
 ('Hildagarde', 'female'),
 ('Abelard', 'male'),
 ...]
```

#### ㄴ. feature 추출 (마지막 글자)
```python
def gender_features(word):
        return {'last_letter': word[-1]}
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
featuresets
```
```
[({'last_letter': 'i'}, 'male'),
 ({'last_letter': 'e'}, 'female'),
 ({'last_letter': 'e'}, 'female'),
 ({'last_letter': 'u'}, 'female'),
 ({'last_letter': 'y'}, 'female'),
 ({'last_letter': 's'}, 'male'),
 ({'last_letter': 'a'}, 'female'),
 ({'last_letter': 'a'}, 'female'),
 ({'last_letter': 'a'}, 'female'),
 ({'last_letter': 'e'}, 'female'),
 ...]
```
#### ㄷ. classifier training
```python
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Gender Classification:", nltk.classify.accuracy(classifier, test_set))
```
```
Gender Classification: 0.744
```
```python
classifier.classify(gender_features('Neo'))
```
```
'male'
```
```python
classifier.classify(gender_features('Trinity'))
```
```
'female'
```
```python
classifier.show_most_informative_features(5)
```
```
Most Informative Features
             last_letter = 'k'              male : female =     44.6 : 1.0
             last_letter = 'a'            female : male   =     34.6 : 1.0
             last_letter = 'p'              male : female =     20.7 : 1.0
             last_letter = 'f'              male : female =     17.1 : 1.0
             last_letter = 'v'              male : female =     11.1 : 1.0
```

#### ㄹ. nltk.classify.apply_features
- 데이터의 크기가 큰 경우 모든 feature를 list로 메모리에 저장하지 않아도 되는 방법

### 2) Choosing the Right Features
- underfit (degree=1)
- ideal fit (degree=3)
- overfit (degree=20)

#### ㄱ. Overfitting Example
```python
def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
```
```
0.762
```
정확도가 더 좋아짐 (?)  
쓸데없는 feature들이 추가한 후 정확도가 더 안좋아져야 정상  

### 3) Refinng the Feature Set: Error Analysis
development set을 추가함  
→ 뭐가 잘못됐는지 확인하는 용도  

#### ㄱ. Train Set
```python
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]
```
```python
train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))
```
```
0.746
```

#### ㄴ. Error Analysis
```python
errors = []
for (name, tag) in devtest_names:
     guess = classifier.classify(gender_features(name))
     if guess != tag: # 머신의 추측이 틀린 경우
         errors.append( (tag, guess, name) )
for (tag, guess, name) in sorted(errors):
     print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))
```
```
correct=female   guess=male     name=Agnes                         
correct=female   guess=male     name=Aleen                         
correct=female   guess=male     name=Alix                          
correct=female   guess=male     name=Allyn                         
correct=female   guess=male     name=Aryn                          
correct=female   guess=male     name=Astrix                        
correct=female   guess=male     name=Avis                          
correct=female   guess=male     name=Bren                          
correct=female   guess=male     name=Brenn                         
correct=female   guess=male     name=Brigit
...
```

#### ㄷ. Improving the classifier set
```python
def gender_features(word):
     return {'suffix1': word[-1:],
             'suffix2': word[-2:]}
```
```python
train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))
```
```
0.762
```
정확도가 향상됨  

