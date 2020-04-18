# Accessing Text Corpora

## Corpus(말뭉치)
- 자연언어 연구를 위해 특정한 목적으로 언어의 표본을 추출한 집합
  - 확률/통계적 기법과 시계열적인 접근으로 전체를 파악함
  - 언어의 빈도와 분포를 확인할 수 있는 자료이며, 현대 언어학 연구에 필수적인 자료
- 언어 연구를 더 효과적으로 하기 위해 말뭉치 **주석**이라는 과정을 거치기도 함
  - 말뭉치 단어의 예-품사 표시(part-of-speech tagging, POS-tagging): 각 단어의 품사 표시(동사, 명사, 형용사 등)에 대한 정보가 말뭉치에 'TAG' 형태로 추가
- 어떤 말뭉치는 한층 더 구조적인 수준의 분석이 적용됨
  - 구문 분석이 완전히 이루어지는 말뭉치들을 **트리뱅크**(Trheebank) 혹은 **분석된 말뭉치**(parsed corpora)라고 함
  - 형태론, 의미론 또는 화용론적 주석을 포함하는 다른 수준의 언어학적 구조 분석이 가능
- 말뭉치는 **은닉 마코프 모델**(Hidden Markov Model, HMM)을 만들어 사용하는 전산 언어학, 음성 인식, 기계 번역 분야의 연구 대상이다.

## Corpus Reader Classes
nltk의 class
1. PlaintextCorpusReader
2. BracketParseCorpusReader

### 1) Automatically Created Corpus Reader Instances
```python
import nltk
from nltk.corpus import *
```
```python
brown
```
```
<CategorizedTaggedCorpusReader in '.../corpora/brown' (not loaded yet)>
```

### 2) raw(), words(), sents(), paras()
```python
import nltk
from nltk.corpus import inaugural
type(inaugural)
```
```
<class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
```
#### raw()
```python
inaugural.raw('1789-Washington.txt')
```
```
'Fellow-Citizens of the Senate and of the House of Representatives:\n\nAmong the ...
```
```python
len(inaugural.raw('1789-Washington.txt'))
```
```
8019
```
#### words()
```python
inaugural.words('1789-Washington.txt')
```
```
['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', ...]
```
```python
len(inaugural.words('1789-Washington.txt'))
```
```
1538
```
```python
word1 = inaugural.words('1789-Washington.txt')
word1[10:20]
```
```
['of', 'Representatives', ':', 'Among', 'the', 'vicissitudes', 'incident', 'to', 'life', 'no']
```
#### sents()
```python
inaugural.sents('1789-Washington.txt')
```
```
[['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', 'and', 'of', 'the', 'House', 'of', 'Representatives', ':'], ['Among', 'the', 'vicissitudes', 'incident', 'to', 'life', 'no', 'event', 'could', 'have', 'filled', 'me', 'with', 'greater', 'anxieties', 'than', 'that', 'of', 'which', 'the', 'notification', 'was', 'transmitted', 'by', 'your', 'order', ',', 'and', 'received', 'on', 'the', '14th', 'day', 'of', 'the', 'present', 'month', '.'], ...]
```
```python
sent1 = inaugural.sents('1789-Washington.txt')
sent1[5]
```
```
['All', 'I', 'dare', 'hope', 'is', 'that', 'if', ',', 'in', 'executing', 'this', 'task', ',', 'I', 'have', 'been', 'too', 'much', 'swayed', 'by', 'a', 'grateful', 'remembrance', 'of', 'former', 'instances', ',', 'or', 'by', 'an', 'affectionate', 'sensibility', 'to', 'this', 'transcendent', 'proof', 'of', 'the', 'confidence', 'of', 'my', 'fellow', 'citizens', ',', 'and', 'have', 'thence', 'too', 'little', 'consulted', 'my', 'incapacity', 'as', 'well', 'as', 'disinclination', 'for', 'the', 'weighty', 'and', 'untried', 'cares', 'before', 'me', ',', 'my', 'error', 'will', 'be', 'palliated', 'by', 'the', 'motives', 'which', 'mislead', 'me', ',', 'and', 'its', 'consequences', 'be', 'judged', 'by', 'my', 'country', 'with', 'some', 'share', 'of', 'the', 'partiality', 'in', 'which', 'they', 'originated', '.']
```
#### paras()
```python
inaugural.paras('1789-Washington.txt')
```
```
[[['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', 'and', 'of', 'the', 'House', 'of', 'Representatives', ':']], [['Among', 'the', 'vicissitudes', 'incident', 'to', 'life', 'no', 'event', 'could', 'have', 'filled', 'me', 'with', 'greater', 'anxieties', 'than', 'that', 'of', 'which', 'the', 'notification', 'was', 'transmitted', 'by', 'your', 'order', ',', 'and', 'received', 'on', 'the', '14th', 'day', 'of', 'the', 'present', 'month', '.'], ['On', 'the', 'one', 'hand', ',', 'I', 'was', 'summoned', 'by', 'my', 'Country', ',', 'whose', 'voice', 'I', 'can', 'never', 'hear', 'but', 'with', 'veneration', 'and', 'love', ',', 'from', 'a', 'retreat', 'which', 'I', 'had', 'chosen', 'with', 'the', 'fondest', 'predilection', ',', 'and', ',', 'in', 'my', 'flattering', 'hopes', ',', 'with', 'an', 'immutable', 'decision', ',', 'as', 'the', 'asylum', 'of', 'my', 'declining', 'years', '--', 'a', 'retreat', 'which', 'was', 'rendered', 'every', 'day', 'more', 'necessary', 'as', 'well', 'as', 'more', 'dear', 'to', 'me', 'by', 'the', 'addition', 'of', 'habit', 'to', 'inclination', ',', 'and', 'of', 'frequent', 'interruptions', 'in', 'my', 'health', 'to', 'the', 'gradual', 'waste', 'committed', 'on', 'it', 'by', 'time', '.'], ['On', 'the', 'other', 'hand', ',', 'the', 'magnitude', 'and', 'difficulty', 'of', 'the', 'trust', 'to', 'which', 'the', 'voice', 'of', 'my', 'country', 'called', 'me', ',', 'being', 'sufficient', 'to', 'awaken', 'in', 'the', 'wisest', 'and', 'most', 'experienced', 'of', 'her', 'citizens', 'a', 'distrustful', 'scrutiny', 'into', 'his', 'qualifications', ',', 'could', 'not', 'but', 'overwhelm', 'with', 'despondence', 'one', 'who', '(', 'inheriting', 'inferior', 'endowments', 'from', 'nature', 'and', 'unpracticed', 'in', 'the', 'duties', 'of', 'civil', 'administration', ')', 'ought', 'to', 'be', 'peculiarly', 'conscious', 'of', 'his', 'own', 'deficiencies', '.'], ['In', 'this', 'conflict', 'of', 'emotions', 'all', 'I', 'dare', 'aver', 'is', 'that', 'it', 'has', 'been', 'my', 'faithful', 'study', 'to', 'collect', 'my', 'duty', 'from', 'a', 'just', 'appreciation', 'of', 'every', 'circumstance', 'by', 'which', 'it', 'might', 'be', 'affected', '.'], ['All', 'I', 'dare', 'hope', 'is', 'that', 'if', ',', 'in', 'executing', 'this', 'task', ',', 'I', 'have', 'been', 'too', 'much', 'swayed', 'by', 'a', 'grateful', 'remembrance', 'of', 'former', 'instances', ',', 'or', 'by', 'an', 'affectionate', 'sensibility', 'to', 'this', 'transcendent', 'proof', 'of', 'the', 'confidence', 'of', 'my', 'fellow', 'citizens', ',', 'and', 'have', 'thence', 'too', 'little', 'consulted', 'my', 'incapacity', 'as', 'well', 'as', 'disinclination', 'for', 'the', 'weighty', 'and', 'untried', 'cares', 'before', 'me', ',', 'my', 'error', 'will', 'be', 'palliated', 'by', 'the', 'motives', 'which', 'mislead', 'me', ',', 'and', 'its', 'consequences', 'be', 'judged', 'by', 'my', 'country', 'with', 'some', 'share', 'of', 'the', 'partiality', 'in', 'which', 'they', 'originated', '.']], ...]
```

## 1. Gutenberg Corpus
```python
from nltk.corpus import gutenberg
gutenberg.fileids()
```
```
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
```

#### 각 파일별 길이 알아내기
```python
for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid))
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
	print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
```
```
5 25 26 austen-emma.txt
5 26 17 austen-persuasion.txt
5 28 22 austen-sense.txt
4 34 79 bible-kjv.txt
5 19 5 blake-poems.txt
4 19 14 bryant-stories.txt
4 18 12 burgess-busterbrown.txt
4 20 13 carroll-alice.txt
5 20 12 chesterton-ball.txt
5 23 11 chesterton-brown.txt
5 18 11 chesterton-thursday.txt
4 21 25 edgeworth-parents.txt
5 26 15 melville-moby_dick.txt
5 52 11 milton-paradise.txt
4 12 9 shakespeare-caesar.txt
4 12 8 shakespeare-hamlet.txt
4 12 7 shakespeare-macbeth.txt
5 36 12 whitman-leaves.txt
```

## 2. Web Text
```python
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:30], '...')
```
```
firefox.txt Cookie Manager: "Don't allow s ...
grail.txt SCENE 1: [wind] [clop clop clo ...
overheard.txt White guy: So, do you have any ...
pirates.txt PIRATES OF THE CARRIBEAN: DEAD ...
singles.txt 25 SEXY MALE, seeks attrac old ...
wine.txt Lovely delicate, fragrant Rhon ...
```

## 3. Chat Text
```python
from nltk.corpus import nps_chat
nps_chat.fileids()
```
```
['10-19-20s_706posts.xml', '10-19-30s_705posts.xml', '10-19-40s_686posts.xml', '10-19-adults_706posts.xml', '10-24-40s_706posts.xml', '10-26-teens_706posts.xml', '11-06-adults_706posts.xml', '11-08-20s_705posts.xml', '11-08-40s_706posts.xml', '11-08-adults_705posts.xml', '11-08-teens_706posts.xml', '11-09-20s_706posts.xml', '11-09-40s_706posts.xml', '11-09-adults_706posts.xml', '11-09-teens_706posts.xml']
```
```python
chatroom = nps_chat.posts('10-19-30s_705posts.xml')
chatroom[100]
```
```
['i', 'like', 'mine', 'shook', 'over', 'ice']
```

## 4. Brown Corpus: Genre
```python
type(brown)
```
```
<class 'nltk.corpus.util.LazyCorpusLoader'>
```
```python
brown.words()
type(brown)
```
```
<class 'nltk.corpus.reader.tagged.CategorizedTaggedCorpusReader'>
```
- gutenberg보다 method들이 더 많음

```python
from nltk.corpus import brown
brown.categories()
```
```
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
```
```python
brown.words(categories='news')
```
```
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
```
```python
brown.words(fileids=['cg22'])
```
```
['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]
```
```python
brown.sents(categories=['news','editorial'])
```
```
[['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', 'Friday', 'an', 'investigation', 'of', "Atlanta's", 'recent', 'primary', 'election', 'produced', '``', 'no', 'evidence', "''", 'that', 'any', 'irregularities', 'took', 'place', '.'], ['The', 'jury', 'further', 'said', 'in', 'term-end', 'presentments', 'that', 'the', 'City', 'Executive', 'Committee', ',', 'which', 'had', 'over-all', 'charge', 'of', 'the', 'election', ',', '``', 'deserves', 'the', 'praise', 'and', 'thanks', 'of', 'the', 'City', 'of', 'Atlanta', "''", 'for', 'the', 'manner', 'in', 'which', 'the', 'election', 'was', 'conducted', '.'], ...]
```
```python
brown.fileids()
```
```
['ca01', 'ca02', 'ca03', 'ca04', 'ca05', 'ca06', 'ca07', 'ca08', 'ca09', 'ca10', ...]
```

### FreqDist()
```python
sciFi = brown.words(categories='science_fiction')
fdist = nltk.FreqDist([len(w) for w in sciFi])
print(fdist)
```
```
<FreqDist with 21 samples and 14470 outcomes>
```
```python
fdist.keys()
```
```
dict_keys([3, 4, 2, 7, 6, 8, 1, 5, 9, 16, 12, 10, 13, 15, 11, 14, 19, 18, 21, 17, 27])
```
```python
fdist = nltk.FreqDist([w.lower() for w in sciFi])
print(fdist)
```
```
<FreqDist with 3032 samples and 14470 outcomes>
```
```python
fdist['alien']
```
```
3
```
```python
fdist.freq('alien')
```
```
0.0002073255010366275
```

### 빈도수 분포 (Frequency Distribution)
```python
nltk.FreqDist
```
```
<class 'nltk.probability.FreqDist'>
```
```python
bWordsFreqDist = nltk.FreqDist(brown.words())
bWordsFreqDist
```
```
FreqDist({'the': 62713, ',': 58334, '.': 49346, 'of': 36080, 'and': 27915, 'to': 25732, 'a': 21881, 'in': 19536, 'that': 10237, 'is': 10011, ...})
```
Brown corpus에서는 'the'라는 단어가 62713번 나옴  

### Conditional Frequency Distribution
category 별로 빈도수를 세고 싶을 때 사용  

```python
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genres, samples=modals)
```
### 장르별 임의의 단어 분포 조사

```python
x = ['love', 'president', 'funny', 'crime', 'god']
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
cfd.tabulate(conditions=brown.categories, samples=x)
```

## 5. Reuters Corpus
- Multiple Categories
- 하나의 파일에 여러가지 카테고리가 붙음
- training/test로 나누어져 있음

## 6. Inaugural Address Corpus
파일에 연도가 붙어있음  
```python
from nltk.corpus import inaugural
inaugural.fileids()
```
```
['1789-Washington.txt', '1793-Washington.txt', '1797-Adams.txt', '1801-Jefferson.txt', '1805-Jefferson.txt', '1809-Madison.txt', '1813-Madison.txt', '1817-Monroe.txt', '1821-Monroe.txt', '1825-Adams.txt', '1829-Jackson.txt', '1833-Jackson.txt', '1837-VanBuren.txt', '1841-Harrison.txt', '1845-Polk.txt', '1849-Taylor.txt', '1853-Pierce.txt', '1857-Buchanan.txt', '1861-Lincoln.txt', '1865-Lincoln.txt', '1869-Grant.txt', '1873-Grant.txt', '1877-Hayes.txt', '1881-Garfield.txt', '1885-Cleveland.txt', '1889-Harrison.txt', '1893-Cleveland.txt', '1897-McKinley.txt', '1901-McKinley.txt', '1905-Roosevelt.txt', '1909-Taft.txt', '1913-Wilson.txt', '1917-Wilson.txt', '1921-Harding.txt', '1925-Coolidge.txt', '1929-Hoover.txt', '1933-Roosevelt.txt', '1937-Roosevelt.txt', '1941-Roosevelt.txt', '1945-Roosevelt.txt', '1949-Truman.txt', '1953-Eisenhower.txt', '1957-Eisenhower.txt', '1961-Kennedy.txt', '1965-Johnson.txt', '1969-Nixon.txt', '1973-Nixon.txt', '1977-Carter.txt', '1981-Reagan.txt', '1985-Reagan.txt', '1989-Bush.txt', '1993-Clinton.txt', '1997-Clinton.txt', '2001-Bush.txt', '2005-Bush.txt', '2009-Obama.txt', '2013-Obama.txt', '2017-Trump.txt']
```
```python
[fileid[:4] for fileid in inaugural.fileids()]
```
```
['1789', '1793', '1797', '1801', '1805', '1809', '1813', '1817', '1821', '1825', '1829', '1833', '1837', '1841', '1845', '1849', '1853', '1857', '1861', '1865', '1869', '1873', '1877', '1881', '1885', '1889', '1893', '1897', '1901', '1905', '1909', '1913', '1917', '1921', '1925', '1929', '1933', '1937', '1941', '1945', '1949', '1953', '1957', '1961', '1965', '1969', '1973', '1977', '1981', '1985', '1989', '1993', '1997', '2001', '2005', '2009', '2013', '2017']
```
#### America와 Citizen의 분포 확인
```python
x = [(target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target)] # americans, citizens, etc...도 횟수 셈
len(x)
```
```
729
```
```python
list(x)
```
```
[('citizen', '1789'), ('citizen', '1789'), ('citizen', '1789'), ('citizen', '1789), ...]
```

```python
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # fileid 앞 4글자(년도)
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target)
)
```

## 7. Loading your own corpus
### 1) PlaintextCorpusReader
```python
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root,'.*')
wordlists.fileids()
wordlists.words('connectives')
```

### 2) BracketParsecorpusReader
```python
from nltk.corpus import BracketParseCorpusReader
corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
file_pattern = r".*/wsj_.*\.mrg"
ptb = BracketParseCorpusReader(corpus_root,file_pattern)
ptb.fileids()
len(ptb.sents())
ptb.sents(fileids='20/wsj_2013.mrg')[19]
```

## 8. Genomics & Informatics (PlaintextCorpusReader)
```python
from nltk.corpus import *
corpus_root = "C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw"
GNICorpus = PlaintextCorpusReader(corpus_root, '.*\.txt', encoding='utf-8')
GNICorpus.fileids()
```
```
['gi-2017-15-3-81.txt', 'gi-2017-15-3-82.txt', 'gi-2017-15-4-113.txt', 'gi-2017-15-4-114.txt', 'gi-2017-15-4-123.txt', ... ]
```
```python
GNICorpus.raw('gni-6-1-1.txt')
```
```
"\n=============Title==========\nCopy Number Variations in the Human Genome: Potential Source for Individual Diversity and Disease Association Studies.\n=============Cor Author==========\n*Corresponding author: E-mail yejun@catholic.ac.krTel +82-2-590-1214, Fax +82-2-596-8969 Accepted 11 March 2008\n===========Auth ... "
```
