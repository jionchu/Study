# Normalizing Text

## 1. Stemming vs Lemmatization
- Stemming: 규칙 기반
- Lemmatization: 사전 기반 -> stemming보다 진화한 형태

### 1) NLTK Stemmers
```python
tokens = nltk.word_tokenize(raw)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
```
#### ㄱ. porter
```python
[porter.stem(t) for t in tokens]
```
```
['=============title==========',
 'copi',
 'number',
 'variat',
 'in',
 'the',
 'human',
 'genom',
 ':',
 'potenti',
 'sourc',
 'for',
 'individu',
 'divers',
 'and', 'freeman',
 'et',
 'al.',
 ',',
 '2006',
 ')',
 '.',
 'smaller',
 'variat',
 'such',
 'as',
 'small',
 'insertional-',
 ...]
```

#### ㄴ. landcaster
```python
[lancaster.stem(t) for t in tokens]
```
```
['=============title==========',
 'cop',
 'numb',
 'vary',
 'in',
 'the',
 'hum',
 'genom',
 ':',
 'pot',
 'sourc',
 'for',
 'individ',
 'divers',
 'and',
 'diseas',
 'assocy',
 'freem',
 'et',
 'al.',
 ',',
 '2006',
 ')',
 '.',
 'smal',
 'vary',
 'such',
 'as',
 'smal',
 'insertional-',
 ...]
```

### 2) NLTK Lemmatizers
```python
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]
```
```
['=============Title==========',
 'Copy',
 'Number',
 'Variations',
 'in',
 'the',
 'Human',
 'Genome',
 ':',
 'Potential',
 'Source',
 'for',
 'Individual',
 'Diversity',
 'and',
 'Disease',
 'Association',
 'Freeman',
 'et',
 'al.',
 ',',
 '2006',
 ')',
 '.',
 'Smaller',
 'variation',
 'such',
 'a',
 'small',
 'insertional-',
 ...]
```

### 3) G&I 논문별로 빈도수 많은 단어부터 출력
(stop words 제거 및 lemmatizer 적용)

#### ㄱ. lemmatizer
```python
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
wnl = nltk.WordNetLemmatizer()
wnl.lemmatize('genes')
```
```
'gene'
```

#### ㄴ. stop words (의미 없는 단어들) 제거
```python
from nltk.corpus import stopwords
words = ['the','adenovirus','E1A243b','protein','can','activate','transcription','of','the','mouse','c-fos','gene','in','a','manner','that','depends','on']
[x for x in words if not (x in stopwords.words('english'))]
```
```
['adenovirus',
 'E1A243b',
 'protein',
 'activate',
 'transcription',
 'mouse',
 'c-fos',
 'gene',
 'manner',
 'depends']
```

## 2. Tokenizing

### 1) Simple Approach to Tokenizaation
```python
raw = '''I'm feeling "hot-tempered".'''
re.split(r' ',raw)
```
```
["I'm", 'feeling', '"hot-tempered".']
```
```python
re.split(r'[\t\n]+',raw)
```
```
["I'm", 'feeling', '"hot-tempered".']
```
```python
re.split(r'\W+',raw)
```
```
['I', 'm', 'feeling', 'hot', 'tempered', '']
```
```python
re.findall(r'\w+|\S\w*',raw)
```
```
['I', "'m", 'feeling', '"hot', '-tempered', '"', '.']
```
```python
re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",raw)
```
```
["I'm", 'feeling', '"hot', '-', 'tempered', '"', '.']
```

### 2) NLTK's Regular Expression Tokenizer
```python
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x) # set flag to allow verbose regexps
    ([A-Z]W.)+
    | \w+(-\w+)*
    | \$?\d+(\.\d+)?%?
    | \.\.\.
    | [][.,;"'?():-_`]
    '''
nltk.regexp_tokenize(text, pattern)
```

### 3) nltk.regexp_tokenize()를 활용하여 GNI 코퍼스 토큰화
```python
corpus_root = "C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw"
gni = PlaintextCorpusReader(corpus_root, '.*\.txt', encoding='utf-8')
pattern = r'''(?x) # set flag to allow verbose regexps
    ([A-Z]W.)+
    | \w+(-\w+)*
    | \$?\d+(\.\d+)?%?
    | \.\.\.
    | [][.,;"'?():-_`]
    '''
giRaw = GNICorpus.raw('gni-6-1-1.txt')
tokenized_giRaw = nltk.regexp_tokenize(giRaw, pattern)
tokenized_giRaw[1000:1100]
```

## 3. Segmentation
### 1) Simple Approach to Segmentation
```python
GNI = PlaintextCorpusReader("C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw", '.*\.txt', encoding='utf-8')
giRaw = GNI.raw('gni-6-1-1.txt')
giWords = GNI.words('gni-6-1-1.txt')
giWords2 = re.split(r'[ \n\t]+',giRaw)
```
#### ㄱ. words
```python
len(giWords)
```
```
2638
```
```python
giWords[200:250]
```
```
['reports',
 'on',
 'CNVs',
 ',',
 'it',
 'is',
 'now',
 'evident',
 'that',
 'these',
 'variants',
 'contribute',
 'significantly',
 'to',
 'genetic',
 'diversity',
 'in',
 'the',
 'human',
 'genome',
 '.',
 'Like',
 'single',
 'nucleotide',
 'polymorphisms',
 '(',
 'SNPs',
 '),',
 'CNVs',
 'are',
 'expected',
 'to',
 'serve',
 'as',
 'potential',
 'biomarkers',
 'for',
 'disease',
 'susceptibility',
 'or',
 'drug',
 'responses',
 '.',
 'However',
 ',',
 'the',
 'technical',
 'and',
 'practical',
 'concerns']

```
#### ㄴ. split
```python
len(giWords2)
```
```
2140
```
```python
giWords2[200:250]
```
```
['of',
 'platforms',
 'that',
 'are',
 'available',
 'at',
 'the',
 'moment',
 'and',
 'suggest',
 'the',
 'potential',
 'of',
 'CNVs',
 'in',
 'clinical',
 'research',
 'and',
 'application.',
 'IIntroduction.',
 'Traditionally,',
 'large-scale',
 'genomic',
 'variants',
 'that',
 'are',
 'visible',
 'in',
 'conventional',
 'karyotyping',
 'have',
 'been',
 'thought',
 'to',
 'be',
 'associated',
 'with',
 'early-onset,',
 'highly',
 'penetrant',
 'genetic',
 'disorders,',
 'while',
 'they',
 'are',
 'incompatible',
 'in',
 'normal,',
 'disease-free',
 'individuals']
```

### 2) Sentence Segmentation
```python
GNI = PlaintextCorpusReader("C://Users/user/Desktop/Genomics-Informatics-Corpus/GNI Corpus 1.0/raw", '.*\.txt', encoding='utf-8')
GNISents = nltk.sent_tokenize(GNI.raw())
GNISents[0]
```
```
'\n=============Title==========\nEditor’s Introduction to This Issue (G&I 15:3, 2017).'
```
```python
GNISents[50]
```
```
'In this study, more pathogenic duplications were observed than deletions (22 vs.   19).'
```
```python
GNISents[100]
```
```
'In addition, the recent discovery that DSBs and subsequent amplification of estrogen response elements can be generated by estrogen- induced long-range chromatin interactions in breast cancer [26] further indicates the importance of higher-order genome architecture for chromosomal rearrangement.'
```

## 4. Formatting
### 1) Writing Results to a File
```python
output_file = open('output.txt','w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    print(word, file=output_file)
```