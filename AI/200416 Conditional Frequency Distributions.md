# Conditional Frequency Distributions

- (condition, event) 형식의 데이터만 conditional frequency distribution 분석이 가능함

## 1. GNI 논문/연도별로 단어 빈도 확인
### 1) corpus 만들기
```python
import nltk
from nltk.corpus import *
corpus_root = "C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw"
GenomInfoCorpus = PlaintextCorpusReader(corpus_root, 'gni.*\.txt', encoding='utf-8')
```
#### 파일 개수
```python
len(GenomInfoCorpus.fileids())
```
```
328
```
#### 코퍼스 파일별 글자 수, 단어 수, 문장 수 통계
```python
for fileid in GenomInfoCorpus.fileids():
    numChars = len(GenomInfoCorpus.raw(fileid))
    numWords = len(GenomInfoCorpus.words(fileid))
    print(fileid,":",numChars,numWords)
```
```
...
gni-9-4-143.txt : 158611 29370
gni-9-4-152.txt : 159073 29465
gni-9-4-161.txt : 159679 29587
gni-9-4-173.txt : 159708 29593
gni-9-4-181.txt : 160206 29691
gni-9-4-189.txt : 160887 29811
gni-9-4-194.txt : 161336 29897
gni-9-4-197.txt : 161685 29946
```

### 2) condition 만들기
```python
x = [(target, fileid[4:6])
    for fileid in GenomInfoCorpus.fileids()
    for w in GenomInfoCorpus.words(fileid)
    for target in ['expression','algorithm','alignments','cancer','patient','genome']
    if w.lower().startswith(target)]
```
```python
type(x), len(x)
```
```
(<class 'list'>, 23002)
```
```python
x[1:20]
```
```
[('expression', '10'), ('expression', '10'), ('genome', '10'), ('genome', '10'), ('genome', '10'), ('expression', '10'), ('genome', '10'), ('genome', '10'), ('genome', '10'), ('expression', '10'), ('genome', '10'), ('genome', '10'), ('genome', '10'), ('expression', '10'), ('expression', '10'), ('genome', '10'), ('genome', '10'), ('genome', '10'), ('genome', '10')]
```

### 3) Conditional Frequency Distribution 구하기
```python
cfd = nltk.ConditionalFreqDist(x)
type(cfd)
```
```
<class 'nltk.probability.ConditionalFreqDist'>
```
```python
cfd['cancer']
```
```
FreqDist({'9-': 972, '8-': 715, '7-': 628, '6-': 480, '11': 373, '10': 309, '12': 286, '13': 220, '14': 87})
```
```python
cfd.plot()
```
![conditional freq dist](https://github.com/jionchu/TIL/blob/master/AI/images/conditional_frequency_distribution.PNG)  

## 2. Random Text with Bigrams
```python
text = nltk.corpus.gutenberg.words('austen-emma.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
cfd['living']
```
```
FreqDist({'with':3,'in':3,'together':2,',':2,'alone':1,'child':1,...})
```

## 3. Lexical Resources
### 1) stop words (document classification)
- high-frequency words
- usually have little lexical content
- 다른 text와 구별하는 것을 어렵게 만들기 때문에 미리 삭제하는 것이 좋음

```python
from nltk.corpus import stopwords
stopwords.words('english')
```
```
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
```
```python
stopwords = nltk.corpus.stopwords.words('english')
reuter = nltk.corpus.reuters.words()
filteredReuter = [w for w in reuter if w.lower() not in stopwords]
len(reuter),len(filteredReuter)
```
```
(1720901, 1265276)
```

### 2) Puzzle Quiz
![quiz puzzle](https://github.com/jionchu/TIL/blob/master/AI/images/quiz_puzzle.PNG)  
```python
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w)>=6
    and obligatory in w
    and nltk.FreqDist(w) <= puzzle_letters]
```

### 3) 영어 중성 이름 찾기
```python
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]
```
```
['Abbey', 'Abbie', 'Abby', 'Addie', 'Adrian', 'Adrien', 'Ajay', 'Alex', 'Alexis', 'Alfie', 'Ali', 'Alix', 'Allie', 'Allyn', 'Andie', 'Andrea', 'Andy', 'Angel', 'Angie', 'Ariel', 'Ashley', 'Aubrey', 'Augustine', 'Austin', 'Averil', 'Barrie', 'Barry', 'Beau', 'Bennie', 'Benny', 'Bernie', 'Bert', 'Bertie', 'Bill', 'Billie', 'Billy', 'Blair', 'Blake', 'Bo', 'Bobbie', 'Bobby', 'Brandy', 'Brett', 'Britt', 'Brook', 'Brooke', 'Brooks', 'Bryn', 'Cal', 'Cam', 'Cammy', 'Carey', 'Carlie', 'Carlin', 'Carmine', 'Carroll', 'Cary', 'Caryl', 'Casey', 'Cass', 'Cat', 'Cecil', 'Chad', 'Chris', 'Chrissy', 'Christian', 'Christie', 'Christy', 'Clair', 'Claire', 'Clare', 'Claude', 'Clem', 'Clemmie', 'Cody', 'Connie', 'Constantine', 'Corey', 'Corrie', 'Cory', 'Courtney', 'Cris', 'Daffy', 'Dale', 'Dallas', 'Dana', 'Dani', 'Daniel', 'Dannie', 'Danny', 'Darby', 'Darcy', 'Darryl', 'Daryl', 'Deane', 'Del', 'Dell', 'Demetris', 'Dennie', 'Denny', 'Devin', 'Devon', 'Dion', 'Dionis', 'Dominique', 'Donnie', 'Donny', 'Dorian', 'Dory', 'Drew', 'Eddie',...]
```

### 4) 성별 이름 끝자리 분포
```python
cfd = nltk.ConditionalFreqDist(
    (fileid,name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid)
)
cfd.plot()
```
![last word of name](https://github.com/jionchu/TIL/blob/master/AI/images/last_word_of_name.PNG)  
- most names ending with **a, e, or i** are female
- names ending in h and l are equally likely to be male or female
- names ending in k, o, r, s, and t are likely to be male

## 4. WordNet
- lexical database for the English language
- dictionary designed specifically for natural language processing
- helps us find word senses, synonyms, antonyms, hyponyms, and other information about a word

### 1) Synonym, Synset, Lemmas

#### ㄱ. Synonym
- same meaning
- a. Benz is credited with the invention of the **motorcar**.
- b. Benz is credited with the invention of the **automobile**.

```python
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
```
```
[Synset('car.n.01')]
```

#### ㄴ. synset, lemmas
- The entity car.n.01 is called a **synset**, or "synonym set", a collection of synonymous words (or "**lemmas**")

1. Unambiguous 'motorcar'
```python
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
```
```
[Synset('car.n.01')]
```
```python
wn.synset('car.n.01').lemmas
```
```
<bound method Synset.lemmas of Synset('car.n.01')>
```
```python
wn.synset('car.n.01').lemma_names()
```
```
['car', 'auto', 'automobile', 'machine', 'motorcar']
```
```python
wn.synset('car.n.01').definition()
```
```
'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
```
```python
wn.synset('car.n.01').examples()
```
```
['he needs a car to get to work']
```

2. Ambiguous 'car'
```python
wn.synsets('car')
```
```
[Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'), Synset('cable_car.n.01')]
```
```python
for synset in wn.synsets('car'):
	print(synset.lemma_names())
```
```
['car', 'auto', 'automobile', 'machine', 'motorcar']
['car', 'railcar', 'railway_car', 'railroad_car']
['car', 'gondola']
['car', 'elevator_car']
['cable_car', 'car']
```
```python
wn.lemmas('car')
```
```
[Lemma('car.n.01.car'), Lemma('car.n.02.car'), Lemma('car.n.03.car'), Lemma('car.n.04.car'), Lemma('cable_car.n.01.car')]
```

### 2) Hyponym, Hypernym, Meronym, Holonym
- **상위어**(hypernym): X가 Y의 한 종류이면 Y는 X의 상위어이다.
- **하위어**(hyponym): Y가 X의 한 종류이면 Y는 X의 하위어이다.
- **전체어**(holonym): X가 Y의 부분이면 Y는 X의 전체어이다.
- **부분어**(meronym): Y가 X의 부분이면 Y는 X의 부분어이다.

#### ㄱ. Hypernym, Hyponym
```python
motorcar = wn.synset('car.n.01')
hypo = motorcar.hyponyms()
len(hypo)
```
```
31
```

#### ㄴ. meronym, holonym, antonym
```python
motorcar = wn.synset('car.n.01')
mero = wn.synset('car.n.01').part_meronyms()
len(mero)
```
```
29
```
```python
mero[0:5]
```

### 3) 원형(stem word) 알아내기
```python
lemmatizer.lemmatize(flies',pos='n')
```
```
'fly'
```
```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize('cooking')
```
```
'cooking'
```
```python
lemmatizer.ammatize('cooking',pos='v')
```
```
'cook'
```
```python
lemmatizer.lemmatize('leaves',pos='v')
```
```
'leave'
```
```python
lemmatizer.lemmatize('leaves',pos='n')
```
```
'leaf'
```