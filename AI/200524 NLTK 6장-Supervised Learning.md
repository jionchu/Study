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

## 2. 영화비평 분류하기 Using NaiveBayesClassifier()
moview review가 positive인지 negative인지 판단하기

#### ㄱ. data labeling
```python
import nltk
import random
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories() # positive인지 negative인지 labeling
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
documents[0]
```
```
(['robert',
  'redford',
  "'",
  's',
  'a',
  'river',
  'runs',
  'through',
  'it',
  'is',
  'not',
  'a',
  'film',
  'i',
  'watch',
  'often',
  '.',
  'it',
  ...])
```

#### ㄴ. feature 추출
```python
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000] # 가장 많이 사용된 2000개 단어
word_features[:100]
```
```
['plot',
 ':',
 'two',
 'teen',
 'couples',
 'go',
 'to',
 'a',
 'church',
 'party',
 ',',
 'drink',
 'and',
 'then',
 'drive',
 '.',
 'they',
 'get',
 'into',
 'an',
 'accident',
 'one',
 'of',
 'the',
 'guys',
 'dies',
 'but',
 'his',
 'girlfriend',
 'continues',
 'see',
 'him',
 'in',
 'her',
 ...]
```
```python
def document_features(document):
      document_words = set(document)
      features = {}
      for word in word_features:
              features['contains({})'.format(word)] = (word in document_words)
      return features
featuresets = [(document_features(d), c) for (d,c) in documents]
featuresets[1]
```
```
({'contains(plot)': True,
  'contains(:)': False,
  'contains(two)': False,
  'contains(teen)': False,
  'contains(couples)': False,
  'contains(go)': False,
  'contains(to)': True,
  'contains(a)': True,
  'contains(church)': False,
  'contains(party)': True,
  'contains(,)': True,
  'contains(drink)': False,
  ...})
```

#### ㄷ. classifier train
```python
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Document Classification:", nltk.classify.accuracy(classifier,test_set))
```
```
Document Classification: 0.81
```
```python
classifier.show_most_informative_features(5)
```
```
Most Informative Features
        contains(justin) = True              neg : pos    =      9.6 : 1.0
 contains(unimaginative) = True              neg : pos    =      8.3 : 1.0
     contains(atrocious) = True              neg : pos    =      7.0 : 1.0
          contains(mena) = True              neg : pos    =      7.0 : 1.0
        contains(shoddy) = True              neg : pos    =      7.0 : 1.0
```

### Bag of Words Feature Extraction
단어가 있는지 없는지만 판단

### Word Embedding
① 어떤 단어가 많이 쓰였는지?
- Bag of Words (순서 신경 쓰지 않음)
- TF-IDF (의미 없는 단어 제외)

② 단어가 어떤 순서로 쓰였는지?
- ELMo
- GPT

③ 어떤 단어와 같이 쓰였는지?
- PMI
- Word2Vec

## 3. 품사에 영향을 주는 suffix 활용 Using DecisionTreeClassifier()
```python
from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
        word = word.lower()
        suffix_fdist[word[-1:]] += 1
        suffix_fdist[word[-2:]] += 1
        suffix_fdist[word[-3:]] += 1
common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
common_suffixes
```
```
['e',
 ',',
 '.',
 's',
 'd',
 't',
 'he',
 'n',
 'a',
 'of',
 'the',
 'y',
 'r',
 'to',
 'in',
 'f',
 'o',
 'ed',
 'nd',
 'is',
 ...]
```
#### ㄱ. feature 추출
```python
def pos_features(word):
        features = {}
        for suffix in common_suffixes: # word가 common_suffixes에 속하는지 확인하기
                features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
        return features
tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
featuresets[:10]
```
```
[({'endswith(e)': True,
   'endswith(,)': False,
   'endswith(.)': False,
   'endswith(s)': False,
   'endswith(d)': False,
   'endswith(t)': False,
   'endswith(he)': True,
   'endswith(n)': False,
   'endswith(a)': False,
   'endswith(of)': False,
   'endswith(the)': True,
   'endswith(y)': False,
   'endswith(r)': False,
   'endswith(to)': False,
   ...},
   'AT'),
   ({'endswith(e)': False,
   'endswith(,)': False,
   'endswith(.)': False,
   'endswith(s)': False,
   'endswith(d)': False,
   'endswith(t)': False,
   'endswith(he)': False,
   'endswith(n)': True,
   'endswith(a)': False,
   'endswith(of)': False,
   'endswith(the)': False,
   'endswith(y)': False,
   ...},
   'NP-TL')
   ...
]
```
#### ㄴ. classifier train
```python
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.DecisionTreeClassifier.train(train_set)
print("POS Tagging:", nltk.classify.accuracy(classifier,test_set))
```
```
POS Tagging: 0.62705121829935351
```

## 4. POS Tagging: exploiting context
단어의 previous word도 함께 feature로 저장

#### ㄱ. feature 추출
```python
def pos_features(sentence, i): 
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

pos_features(brown.sents()[0], 8) # investigation
```
```
{'suffix(1)': 'n', 'suffix(2)': 'on', 'suffix(3)': 'ion', 'prev-word': 'an'}
```
```python
print(brown.sents()[0])
```
```
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', 'Friday', 'an', 'investigation', 'of', "Atlanta's", 'recent', 'primary', 'election', 'produced', '``', 'no', 'evidence', "''", 'that', 'any', 'irregularities', 'took', 'place', '.']
```

#### ㄴ. enumerate
indexing이 자동으로 됨
```python
list(enumerate(brown.sents()[0]))
```
```
[(0, 'The'),
 (1, 'Fulton'),
 (2, 'County'),
 (3, 'Grand'),
 (4, 'Jury'),
 (5, 'said'),
 (6, 'Friday'),
 (7, 'an'),
 (8, 'investigation'),
 (9, 'of'),
 (10, "Atlanta's"),
 (11, 'recent'),
 (12, 'primary'),
 (13, 'election'),
 (14, 'produced'),
 (15, '``'),
 (16, 'no'),
 (17, 'evidence'),
 (18, "''"),
 (19, 'that'),
 (20, 'any'),
 (21, 'irregularities'),
 (22, 'took'),
 (23, 'place'),
 (24, '.')]
```

#### ㄷ. classifier train
```python
tagged_sents = brown.tagged_sents(categories='news')
featuresets = []
for tagged_sent in tagged_sents:
     untagged_sent = nltk.tag.untag(tagged_sent)
     for i, (word, tag) in enumerate(tagged_sent):
         featuresets.append( (pos_features(untagged_sent, i), tag) )

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

nltk.classify.accuracy(classifier, test_set)
```
```
0.7891596220785678
```
```python
list(enumerate(tagged_sents[0]))
```
```
[(0, ('The', 'AT')),
 (1, ('Fulton', 'NP-TL')),
 (2, ('County', 'NN-TL')),
 (3, ('Grand', 'JJ-TL')),
 (4, ('Jury', 'NN-TL')),
 (5, ('said', 'VBD')),
 (6, ('Friday', 'NR')),
 (7, ('an', 'AT')),
 (8, ('investigation', 'NN')),
 (9, ('of', 'IN')),
 (10, ("Atlanta's", 'NP$')),
 (11, ('recent', 'JJ')),
 (12, ('primary', 'NN')),
 (13, ('election', 'NN')),
 (14, ('produced', 'VBD')),
 (15, ('``', '``')),
 (16, ('no', 'AT')),
 (17, ('evidence', 'NN')),
 (18, ("''", "''")),
 (19, ('that', 'CS')),
 (20, ('any', 'DTI')),
 (21, ('irregularities', 'NNS')),
 (22, ('took', 'VBD')),
 (23, ('place', 'NN')),
 (24, ('.', '.'))]
```
