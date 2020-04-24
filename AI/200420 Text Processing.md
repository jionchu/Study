# Text Processing

## 1. Text Processing at the Lowest Level
### 1) Capturing User Input
```python
s = input("Enter some text: ")
```
```
Enter some text: On an exceptionally hot evening early in July
```
```python
print("You typed", len(nltk.word_tokenize(s)), "words.")
```
```
You typed 8 words.
```

## 2. Text Processing with Unicode
- \uXXXX
- default가 아닌 다른 걸로 코딩하고 싶은 경우 '# -*- coding: <coding> -*-' 써줘야 함
```python
# -*- coding: <coding> -*-
```
