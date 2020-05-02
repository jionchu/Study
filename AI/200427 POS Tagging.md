# POS (Part of Speech) Tagging
품사 (명사, 동사, 형용사) tagging

- 태깅정보를 이용하여 더 많은 정보를 추출하자

### 1) 태깅(Tagging)
- 원시 말뭉치에서 중의성을 해소하여 부가적인 언어 정보를 부착하는데, 이 정보를 **태그**(tag)라고 하며, 이러한 행위를 태깅이라 한다.
- 한편 태깅을 수행하는 컴퓨터 프로그램을 **태거**(tagger)라고 한다.
- 태그가 부착된 말뭉치를 **부착말뭉치**(tagged corpus)라고 한다.

### 2) Part of Speech Tagging
Jon saw the saw and decided to take it to the table.  
NNP VBD DT  NN  CC  VBD TO  VB  PRR IN  DT  NN

### 3) Full parsing vs Shallow parsing
- Information Extraction을 하기 위해, Full Parsing은 어려우므로, Shallow Parsing을 하여 부분 정보라도 일단 파악함

### 4) 품사 태깅 방법에 관한 두 학파간의 이견
- Rule-Based: Human crafted rules based on lexical and other lignuistic knowledge.
- Learning-Based: Trained on human annotated corpora like the Penn Treebank.

- Statistical models: Hidden Markov Model(HMM), Maximum Entrop Markov Model(MEMM), Conditional Random Field(CRF)
- Rule learning: Transformation Based Learning(TBL)

### 5) POS Tagging Example
#### ㄱ. pos_tag
```python
import nltk
s = ['time','flies','like','an','arrow']
nltk.pos_tag(s)
```
```
[('time', 'NN'),
 ('flies', 'NNS'),
 ('like', 'IN'),
 ('an', 'DT'),
 ('arrow', 'NN')]
```
POS Tagging 제대로 못함
#### ㄴ. tagset='universal'
```python
nltk.pos_tag(s, tagset='universal')
```
```
[('time', 'NOUN'),
 ('flies', 'NOUN'),
 ('like', 'ADP'),
 ('an', 'DET'),
 ('arrow', 'NOUN')]
```
#### ㄷ. tagset 설명
```python
nltk.help.upenn_tagset()
```

## 1. Using a Tagger
### 1) pos_tag()
생각보다 성능은 좋지 않음

```python
import nltk
from nltk.corpus import *
text = nltk.word_tokenize('They refused to permit us to obtain the refuse permit')
nltk.pos_tag(text)
```
```
[('They', 'PRP'),
 ('refused', 'VBD'),
 ('to', 'TO'),
 ('permit', 'VB'),
 ('us', 'PRP'),
 ('to', 'TO'),
 ('obtain', 'VB'),
 ('the', 'DT'),
 ('refuse', 'NN'),
 ('permit', 'NN')]
```

## 2. Tagged Corpora
### 1) str2tuple()
```python
tagged_token = nltk.tag.str2tuple('fly/NN')
tagged_token
```
```
('fly', 'NN')
```

### 2) tagged_words()
품사 리스트가 tuple로 반환됨
#### ㄱ. tagset='universal'
```python
nltk.corpus.brown.tagged_words()
```
```
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
```
```python
nltk.corpus.brown.tagged_words(tagset='universal')
```
```
[('The', 'DET'), ('Fulton', 'NOUN'), ...]
```

#### ㄴ. others
```python
print(nltk.corpus.nps_chat.tagged_words())
```
```
[('now', 'RB'), ('im', 'PRP'), ('left', 'VBD'), ...]
```
```python
nltk.corpus.conll2000.tagged_words()
```
```
[('Confidence', 'NN'), ('in', 'IN'), ('the', 'DT'), ...]
```
```python
nltk.corpus.treebank.tagged_words()
```
```
[('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ...]
```

### 3) Universal Tag Sets
![universal tag sets](https://github.com/jionchu/TIL/blob/master/AI/images/universal_tag_sets.PNG)  

### 4) 브라운 뉴스 카테고리에서 가장 빈번하게 출현하는 품사 리스트하기
```python
brown_news_tagged = nltk.corpus.brown.tagged_words(categories='news',tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common()
```
```
[('NOUN', 30654),
 ('VERB', 14399),
 ('ADP', 12355),
 ('.', 11928),
 ('DET', 11389),
 ('ADJ', 6706),
 ('ADV', 3349),
 ('CONJ', 2717),
 ('PRON', 2535),
 ('PRT', 2264),
 ('NUM', 2166),
 ('X', 92)]
```
```python
tag_fd.plot(cumulative=True)
```

### 5) 명사 앞에 가장 자주 출현하는 단어 찾기
(a[0],a[1]) : ('The','DET'), ('Fulton','NP') ...  
(a,b) : ('N','DET'), ('NP','N') ...  
```python
word_tag_pairs = nltk.bigrams(brown_news_tagged)
noun_preceders = [a[1] for (a,b) in word_tag_pairs if b[1] == 'NOUN']
fdist = nltk.FreqDist(noun_preceders)
[tag for (tag, _) in fdist.most_common()]
```
```
['NOUN',
 'DET',
 'ADJ',
 'ADP',
 '.',
 'VERB',
 'CONJ',
 'NUM',
 'ADV',
 'PRT',
 'PRON',
 'X']
```

### 6) 뉴스 카테고리에서 가장 빈번한 동사군들 찾기
```python
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
[wt[0] for (wt,_) in word_tag_fd.most_common() if wt[1] == 'VERB']
```
```
['is',
 'said',
 'was',
 'are',
 'be',
 'has',
 'have',
 'will',
 'says',
 'would',
 'were',
 'had',
 'been',
 'could',
 "'s",
 'can',
 'do',
 ...
]
```
#### ㄱ. 'yield'가 어떤 품사로 몇 번 쓰였는지
```python
cfd1 = nltk.ConditionalFreqDist(wsj)
cfd1['yield'].most_common()
```
```
[('VERB', 28), ('NOUN', 20)]
```
#### ㄴ. 'cut'이 어떤 품사로 몇 번 쓰였는지
```python
cfd1['cut'].most_common()
```
```
[('VERB', 25), ('NOUN', 3)]
```

### 7) VBD(과거형) and VBN(과거분사형) 태그를 동시에 가지는 단어를 찾고, 그 주변 텍스트 살펴보기
```python
[w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
```
```
['Asked', 'accelerated', 'accepted', 'accused', 'acquired', added', ... ]
```
```python
idx1 = wsj.index(('kicked', 'VBD'))
wsj[idx1-4:idx1+1]
```
```
[('While', 'IN'), ('program', 'NN'), ('trades', 'NNS'), ('swiftly', 'RB'), ('kicked', 'VBD')]
```
```python
idx2 = wsj.index(('kicked', 'VBN'))
wsj[idx2-4:idx2+1]
```
```
[('head', 'NN'), ('of', 'IN'), ('state', 'NN'), ('has', 'VBZ'), ('kicked', 'VBN')]
```

### 8) tagset 중 'NN'으로 시작하는 태그와 관련 단어들 리스트하기 (brown tagset)
```python
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print(tag, tagdict[tag])
```
```
NN [('year', 137), ('time', 97), ('state', 88), ('week', 85), ('man', 72)]
NN$ [("year's", 13), ("world's", 8), ("state's", 7), ("nation's", 6), ("city's", 6)]
NN$-HL [("Golf's", 1), ("Navy's", 1)]
NN$-TL [("President's", 11), ("Administration's", 3), ("Army's", 3), ("League's", 3), ("University's", 3)]
NN-HL [('sp.', 2), ('problem', 2), ('Question', 2), ('cut', 2), ('party', 2)]
NN-NC [('ova', 1), ('eva', 1), ('aya', 1)]
NN-TL [('President', 88), ('House', 68), ('State', 59), ('University', 42), ('City', 41)]
NN-TL-HL [('Fort', 2), ('Mayor', 1), ('Commissioner', 1), ('City', 1), ('Oak', 1)]
NNS [('years', 101), ('members', 69), ('people', 52), ('sales', 51), ('men', 46)]
NNS$ [("children's", 7), ("women's", 5), ("men's", 3), ("janitors'", 3), ("taxpayers'", 2)]
NNS$-HL [("Dealers'", 1), ("Idols'", 1)]
NNS$-TL [("Women's", 4), ("States'", 3), ("Giants'", 2), ("Princes'", 1), ("Bombers'", 1)]
NNS-HL [('Wards', 1), ('deputies', 1), ('bonds', 1), ('aspects', 1), ('Decisions', 1)]
NNS-TL [('States', 38), ('Nations', 11), ('Masters', 10), ('Communists', 9), ('Rules', 9)]
NNS-TL-HL [('Nations', 1)]
```

### 9) 단어로 검색하는 것보다 POS 태그로 검색하는 것이 나은 경우
#### ㄱ. often 단어의 사용법에 대해 연구
```python
brown_learned_text = nltk.corpus.brown.words(categories='learned')
sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a == 'often'))
```
```
[',',
 '.',
 'accomplished',
 'analytically',
 'appear',
 'apt',
 'associated',
 'assuming',
 'became',
 'become',
 'been',
 'began',
 'call',
 'called',
 'carefully',
 'chose',
 'classified',
 'colorful',
 'composed',
 'contain',
 'differed',
 'difficult',
 'encountered',
 'enough',
 'equate',
 'extremely',
 'found',
 'happens',
 'have',
 'ignored',
 'in',
 'involved',
 'more',
 'needed',
 'nightly',
 'observed',
 'of',
 'on',
 'out',
 'quite',
 'represent',
 'responsible',
 'revamped',
 'seclude',
 'set',
 'shortened',
 'sing',
 'sounded',
 'stated',
 'still',
 'sung',
 'supported',
 'than',
 'to',
 'when',
 'work']
```
```python
brown_lrnd_tagged = nltk.corpus.brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()
```
```
VERB  ADV  ADP  ADJ    .  PRT 
  37    8    7    6    4    2 
```

#### ㄴ. "<Verb> to <Verb>" 구문 형태 모두 찾아내기
```python
from nltk.corpus import brown
import nltk

def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2=='TO' and t3.startswith('V')):
            print(w1, w2, w3)

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
```
```
combined to achieve
continue to place
serve to protect
wanted to wait
allowed to place
expected to become
expected to approve
expected to make
intends to make
seek to set
...
```

## 3. Mapping Words to Properties Using Python Dictionaries

### 1) Defining Dictionary
- create a dictionary
```python
pos = {'colorless':'ADJ', 'ideas':'N', 'sleep':'V','furiously':'ADV'}
pos = dict(colorless='ADJ', ideas='N', sleep='V', furiously='ADV')
```
- dictionary keys must be immutable types

```python
import nltk
pos = {'colorless':'ADJ', 'ideas':'N', 'sleep':'V','furiously':'ADV'}
pos['colorless']
```
```
'ADJ'
```
```python
pos['sleep']
```
```
'V'
```
```python
pos['blog']
```
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-14268bca594a> in <module>
----> 1 pos('blog')

TypeError: 'dict' object is not callable
```

### 2) Default dictionary
```python
from collections import defaultdict
pos = defaultdict(lambda:'NOUN')
pos['ideas'] = 'N'
pos
```
```
defaultdict(<function __main__.<lambda>()>, {'ideas': 'N'})
```
```python
pos['ideas']
```
```
'N'
```
```python
pos['blog']
```
```
'NOUN'
```

### 3) 품사 개수 세기
#### ㄱ. 전체 품사 개수 세기
```python
from collections import defaultdict
counts = defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories=
'news', tagset='universal'):
    counts[tag] += 1
```
#### ㄴ. 특정 품사의 개수 알아내기
```python
counts['NOUN']
```
```
30654
```

#### ㄷ. 개수가 많은 순서대로 품사 정렬하기
```python
from operator import itemgetter
sorted(counts.items(), key=itemgetter(1), reverse=True)
```
```
[('NOUN', 30654),
 ('VERB', 14399),
 ('ADP', 12355),
 ('.', 11928),
 ('DET', 11389),
 ('ADJ', 6706),
 ('ADV', 3349),
 ('CONJ', 2717),
 ('PRON', 2535),
 ('PRT', 2264),
 ('NUM', 2166),
 ('X', 92)]
```
```python
[t for t,c in sorted(counts.items(), key=itemgetter(1), reverse=True)]
```
```
['NOUN',
 'VERB',
 'ADP',
 '.',
 'DET',
 'ADJ',
 'ADV',
 'CONJ',
 'PRON',
 'PRT',
 'NUM',
 'X']
```
```python
counts.items()
```
```
dict_items([('DET', 11389), ('NOUN', 30654), ('ADJ', 6706), ('VERB', 14399), ('ADP', 12355), ('.', 11928), ('ADV', 3349), ('CONJ', 2717), ('PRT', 2264), ('PRON', 2535), ('NUM', 2166), ('X', 92)])
```

### 4) Complex Keys and Values
```python
pos = defaultdict(lambda: defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
    pos[(t1, w2)][t2] += 1

// right라는 단어 앞에 DET(관사)가 있는 경우 right의 품사는 무엇인가
pos[('DET', 'right')]
```
```
defaultdict(<class 'int'>, {'ADJ': 11, 'NOUN': 5})
```

### 5) Index words according to their last two letters
```python
last_letters = defaultdict(list)
words = nltk.corpus.words.words('en')
for word in words:
    key = word[-2:]
    last_letters[key].append(word)

last_letters['ly']
```
```
['abactinally',
 'abandonedly',
 'abasedly',
 'abashedly',
 'abashlessly',
 'abbreviately',
 'abdominally',
 'abhorrently',
 ...
]
```
```python
last_letters['zy']
```
```
['blazy',
 'bleezy',
 'blowzy',
 'boozy',
 'breezy',
 'bronzy',
 'buzzy',
 'Chazy',
 'cozy',
 'crazy',
 ...
]
```