# Procedural Python

## 1. 자료형
- Numbers (immutable)
- Sequences
  - String (immutable)
  - Lists (mutable)
  - Tuples (immutable)
  - Dictionaries (mutable)
- Files

### 4개의 주요 데이터 구조
- String, List, Tuple, Dictionary
```python
myString = 'TAAccCtAaccctaaccCTAAccctaacccTAAcc'
myList = ['TAAccCtA','ccct','','ccCTAAccct','','cccTAAcc']
myTuple = ('TAAccCtA',8)
myDictionary = {'UUG':'Leu','AUG':'Met','UAA':'Stop'}
```
### indexing 규칙
1. string
```python
myString[3]
```
```
'c'
```
```python
myString[3:8]
```
```
'ccCtA'
```
2. list
```python
myList[1]
```
```
'ccct'
```
```python
myList[-1]
```
```
'cccTAAcc'
```
3. tuple
```python
myTuple[1]
```
```
8
```
4. dictionary
```python
myDictionary['UUG']
```
```
'Leu'
```
