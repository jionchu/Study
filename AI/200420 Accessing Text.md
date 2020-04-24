# Accessing Text from the Web and from Disk

### NLP Major evaluations and tasks of Syntax
- Lemmatization
- Stemming
- Part-of-speech tagging
- Parsing
- Sentence breaking
- Word segmentation

## 1. Web에서 text 다운받기

### 1) 죄와벌(Crime & Punishment) 다운받기
```python
from urllib import *
```
#### ㄱ. html로 다운
```python
url = "http://www.gutenberg.org/files/2554/2554-h/2554-h.htm"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)
```
```
str
```
```python
raw[:50]
```
```
'<?xml version="1.0" encoding="utf-8"?>\r\n\r\n<!DOCTYP'
```
#### ㄴ. txt로 다운
```python
url2 = "http://www.gutenberg.org/files/2554/2554-0.txt"
response2 = request.urlopen(url2)
raw2 = response2.read().decode('utf8')
len(raw2)
```
```
1176967
```
```python
raw2[:50]
```
```
'\ufeffThe Project Gutenberg EBook of Crime and Punishme'
```

### 2) Removing Header or Footer
#### ㄱ. header 찾기
```python
raw.find("PART I")
```
```
5338
```
#### ㄴ. footer 찾기
```python
raw.rfind("End of Project Gutenberg's Crime")
```
```
1157746
```
#### ㄷ. header와 footer 제거
```python
raw = raw[5338:1157746]
raw.find("PART I")
```
```
0
```

### 3). Dealing with HTML (html 태그 제거)

#### ㄱ. nltk.clean_html
```python
import nltk
nltk.clean_html(raw)
```
```
NotImplementedError                       Traceback (most recent call last)
<ipython-input-19-1bb8ff1f4b1a> in <module>
----> 1 nltk.clean_html(raw)

~\Anaconda3\lib\site-packages\nltk\util.py in clean_html(html)
    391 def clean_html(html):
    392     raise NotImplementedError(
--> 393         "To remove HTML markup, use BeautifulSoup's get_text() function"
    394     )
    395 

NotImplementedError: To remove HTML markup, use BeautifulSoup's get_text() function
```

#### ㄴ. BeautifulSoup4
```python
from bs4 import BeautifulSoup
url = "http://www.gutenberg.org/files/2554/2554-h/2554-h.htm"
html = request.urlopen(url).read().decode('utf8')
html[:100]
```
```
'<?xml version="1.0" encoding="utf-8"?>\r\n\r\n<!DOCTYPE html\r\n   PUBLIC "-//W3C//DTD XHTML 1.0 Strict//E'
```
```python
raw = BeautifulSoup(html,'html.parser').get_text()
raw[:100]
```
```
'\n\n\n\n\r\n      Crime and Punishment, by Fyodor Dostoevsky\r\n    \n\r\n\r\n    body { margin:5%; background:#f'
```

### 4) Dealing with HTML (토큰화)
- tokenization: 굉장히 어려운 문제
```python
tokens = nltk.word_tokenize(raw)
tokens[:30]
```
```
['Crime',
 'and',
 'Punishment',
 ',',
 'by',
 'Fyodor',
 'Dostoevsky',
 'body',
 '{',
 'margin:5',
 '%',
 ';',
 'background',
 ':',
 '#',
 'faebd0',
 ';',
 'text-align',
 ':',
 'justify',
 '}',
 'P',
 '{',
 'text-indent',
 ':',
 '1em',
 ';',
 'margin-top',
 ':',
 '.25em']
```

## 5) Text() 객체 생성
```python
text = nltk.Text(tokens)
type(text)
```
```
nltk.text.Text
```
Text 객체로 변환하면 여러가지 메소드들을 사용할 수 있음
```python
text.collocations()
```
```
Katerina Ivanovna; Pyotr Petrovitch; Pulcheria Alexandrovna; Avdotya
Romanovna; Rodion Romanovitch; Marfa Petrovna; Sofya Semyonovna; old
woman; Project Gutenberg-tm; Porfiry Petrovitch; Amalia Ivanovna;
great deal; young man; Nikodim Fomitch; Ilya Petrovitch; Project
Gutenberg; Andrey Semyonovitch; Hay Market; Dmitri Prokofitch; Good
heavens
```
```python
text.concordance('novel')
```
```
Displaying 2 of 2 matches:
ous day and he knew that a perfectly novel experience had befallen him , that h
ow you ) and the second time a whole novel ( I begged him to let me copy it out
```

## 2. Reading local files: os package
```python
import os
os.getcwd()
os.listdir('.')
os.childir('c://nltk_data/')
os.listdir()
```
