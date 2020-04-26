# Regular Expression

## 1. Regular Expression

|Operator|Behavior|
|:--------|:--------|
|^|이 패턴으로 시작해야 함|
|$|이 패턴으로 종료해야 함|
|[문자들]|문자들 중에 하나이어야 함. 가능한 문자들의 집합|
|[^문자들]|[문자들]의 반대로 피해야할 문자들의 집합을 정의함|
|\||두 패턴 중 하나이어야 함 (OR 기능)|
|?|앞 패턴이 없거나 하나이어야 함 (Optional 패턴을 정의할 때 사용)|
|+|앞 패턴이 하나 이상이어야 함|
|*|앞 패턴이 0개 이상이어야 함|
|패턴{n}|앞 패턴이 n번 반복해서 나타나는 경우|
|패턴{n,m}|앞 패턴이 최소 n번, 최대 m번 반복해서 나타나는 경우 (n 또는 m은 생략 가능)|
|\d|숫자 0~9|
|\w|문자를 의미|
|\s|화이트 스페이스를 의미하는데, [\t\n\r\f]와 동일|
|.|뉴라인(\n)을 제외한 모든 문자를 의미|

```python
import re
import nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
len(wordlist)
```
```
210687
```
#### ㄱ. 특정 패턴으로 시작하는 문자열 찾기
```python
[w for w in wordlist if re.search('^abc',w)]
```
```
['abcoulomb']
```
#### ㄴ. 특정 패턴으로 끝나는 문자열 찾기
```python
[w for w in wordlist if re.search('omics$',w)]
```
```
['aerodromics',
 'agronomics',
 'anthroponomics',
 'astronomics',
 'atomics',
 'bionomics',
 'economics',
 'ethonomics',
 'hydroeconomics',
 'loxodromics',
 'orthodromics',
 'phoronomics',
 'physiognomics',
 'psychonomics',
 'pyronomics',
 'socionomics']
```
#### ㄷ. 패턴 중 하나를 포함하는 문자열 찾기
```
[w for w in wordlist if re.search('[abc][abc][abc][abc][abc]',w)]
```
```
['abaca',
 'abacate',
 'abacay',
 'abbacomes',
 'abbacy',
 ...
 'taccaceous',
 'unscabbard',
 'unscabbarded']
```
#### ㄹ. 패턴이 여러번 반복되는 문자열 찾기
```python
[w for w in wordlist if re.search('aab+',w)]
```
```
['haab', 'staab']
```

### 1) 전화번호 4653으로 만들 수 있는 영어 단어는?
![text on 9 kyes](https://github.com/jionchu/TIL/blob/master/AI/images/text_on_9_kyes.PNG)  

```python
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$',w)]
```
```
['gold', 'golf', 'hold', 'hole']
```

### 2) Chat Corpus with Cleene Closure
```python
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
[w for w in chat_words if re.search('^m+i+n+e+$',w)]
```
```
['miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee',
 'miiiiiinnnnnnnnnneeeeeeee',
 'mine',
 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee']
```
```python
[w for w in chat_words if re.search('^[ha]+$',w)]
```
```
['a',
 'aaaaaaaaaaaaaaaaa',
 'aaahhhh',
 'ah',
 'ahah',
 'ahahah',
 'ahh',
 'ahhahahaha',
 'ahhh',
 'ahhhh',
 'ahhhhhh',
 'ahhhhhhhhhhhhhh',
 'h',
 'ha',
 'haaa',
 'hah',
 'haha',
 'hahaaa',
 'hahah',
 'hahaha',
 'hahahaa',
 'hahahah',
 'hahahaha',
 'hahahahaaa',
 'hahahahahaha',
 'hahahahahahaha',
 'hahahahahahahahahahahahahahahaha',
 'hahahhahah',
 'hahhahahaha']
```

### 3) More Examples
```python
wsj = sorted(set(nltk.corpus.treebank.words()))
[w for w in wsj if re.search('^[0-9]+\.[0-9]+$',w)]
```

## 2. Useful Applications of Regular Expressions

### 1) re 모듈의 메소드들
- **search**(): 주어진 string 전체를 pattern으로 검색하여 일치하는 첫번째 문자열을 찾는다.
- **match**(): 메소드는 주어진 string의 첫 문자열만을 비교하여 pattern과 match되는지를 확인한다. 따라서, serach와 다르게 string의 처음부터 일치하여야 함
- **findall**(): 주어진 string 전체에서 pattern과 일치하는 것을 모두 찾아서 list로 반환
- **sub**(): 주어진 string 전체에서 pattern과 일치하는 모든 것을 replace로 교체하고, 결과를 str 타입으로 반환. replace는 문자열이 될 수도 있고, 함수가 될 수도 있다.
- **split**(): 주어진 string을 pattern으로 분리시키는 기능을 수행한다. 파이썬 string의 기본적인 split으로도 delimiter를 설정, 문자열을 나눌 수 있으나, 하나의 문자가 아닌 특정한 규칙을 지닐 수 있는 정규 표현식을 이용하려면, re.split()을 사용해야 함
- **compile**(): 해당 정규 표현식을 re.RegexObject 객체로 저장할 수 있어 매번 다시 쓰는 번거로움을 피할 수 있음

#### ㄱ. re.findall()
```python
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]',word)
```
```
['u',
 'e',
 'a',
 'i',
 'a',
 'i',
 'i',
 'i',
 'e',
 'i',
 'a',
 'i',
 'o',
 'i',
 'o',
 'u']
```

### 2) GNI 논문 각각의 책임저자 이메일 주소 출력
#### ㄱ. 한 개만 출력
```python
GNI = PlaintextCorpusReader("C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw",  '.*\.txt', encoding='utf-8')
giRaw = GNI.raw('gni-6-1-1.txt')
re.findall(r'[\w._%+=]+@[\w.-]+\.[a-zA-Z]{2,4}',giRaw)
```
```
['yejun@catholic.ac.krTe']
```
#### ㄴ. 전체 출력
```python
import nltk
from nltk import *
from nltk.corpus import *

corpus_root = "C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw"
gni = PlaintextCorpusReader(corpus_root, '.*\.txt', encoding='utf-8')

for file in gni.fileids():
    raw = gni.raw(file)
    print(re.findall(r'[\w._%+=]+@[\w.-]+\.[a-zA-Z]{2,4}',raw))
```
```
['yejun@catholic.ac.kr']
['bluelabelman81@gmail.com']
['yejun@catholic.ac.kr']
['kimty@snu.ac.kr']
['schoi@kangwon.ac.kr']
['sskimb@ssu.ac.kr']
['yejun@catholic.ac.kr']
['MinhoLee@catholic.ac.kr']
['MinhoLee@catholic.ac.kr']
['MinhoLee@catholic.ac.kr']
['sureshkumar@msu.edu.my']
['Mohamad.hajari@gmail.com', 'hajari@scu.ac.ir']
['sskimb@ssu.ac.krTh']
['jongil@snu.ac.kr']
...
```

### 3) GNI 단어들 중 모음이 두개 연이어 나오는 경우의 빈도수 측정
```python
import nltk
from nltk import *
from nltk.corpus import *

corpus_root = "C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw"
gni = PlaintextCorpusReader(corpus_root, '.*\.txt', encoding='utf-8')

import re
words = sorted(set(gni.words()))
fd = nltk.FreqDist(x for word in words for x in re.findall(r'[aeiou]{2,}',word))
fd.items()
```
```
dict_items([('ei', 344), ('ioi', 25), ('ea', 663), ('io', 1660), ('ou', 413), ('ua', 211), ('ia', 651), ('ie', 545), ('oo', 251), ('ee', 276), ('ui', 148), ('iu', 61), ('au', 149), ('ai', 300), ('eae', 14), ('ae', 77), ('eo', 239), ('eu', 169), ('oi', 176), ('ue', 190), ('oa', 92), ('aeo', 4), ('iai', 1), ('aa', 11), ('ao', 15), ('eau', 5), ('oui', 3), ('ioa', 7), ('ioe', 11), ('oe', 43), ('ii', 18), ('uou', 13), ('eou', 19), ('uu', 4), ('eiou', 2), ('uo', 23), ('aue', 4), ('eui', 3), ('oeu', 2), ('iou', 33), ('eio', 8), ('ieu', 2), ('ieae', 1), ('aie', 1), ('eie', 1), ('oai', 1), ('oea', 1), ('iao', 3), ('eoae', 1), ('ooi', 1), ('aea', 2), ('oua', 1), ('eea', 3), ('eei', 3), ('uaeo', 1), ('ueou', 1), ('iae', 2), ('oau', 3), ('oii', 1), ('oie', 4), ('oue', 1), ('iii', 1), ('oae', 1), ('eoa', 1), ('aeu', 1), ('uai', 1), ('uie', 2), ('iau', 1), ('uee', 1)])
```

### 4) rotokas words
```python
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]',w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()
```
```
    a   e   i   o   u 
k 418 148  94 420 173 
p  83  31 105  34  51 
r 187  63  84  89  79 
s   0   0 100   2   1 
t  47   8   0 148  37 
v  93  27 105  48  49 
```

### 5) finding word stems
- siffix, prefix 찾기
```python
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
        return word
```

## 3. NLTK's findall()
- token 단위로 찾아줌
```python
from nltk.corpus import gutenberg, nps_chat
```
#### ㄱ. moby_dick
```python
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r"<a>(<.*>)<man>")
```
```
monied; nervous; dangerous; white; white; white; pious; queer; good;
mature; white; Cape; great; wise; wise; butterless; white; fiendish;
pale; furious; better; certain; complete; dismasted; younger; brave;
brave; brave; brave
```
#### ㄴ. nps_chat
```python
chat = nltk.Text(nps_chat.words())
chat.findall(r"<.*><.*><bro>")
```
```
you rule bro; telling you bro; u twizted bro
```
```python
chat.findall(r"<l.*>{3,}")
```
```
lol lol lol; lmao lol lol; lol lol lol; la la la la la; la la la; la
la la; lovely lol lol love; lol lol lol.; la la la; la la la
```