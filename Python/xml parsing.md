# xml parsing

### xml example
```
<?xml version="1.0" encoding="UTF-8"?>
<sentence><tok cat="1">Hello</tok> <tok cat="2">world</tok></sentence>
<sentence><tok cat="1">xml</tok> <tok cat="2">parsing</tok></sentence>
```

## 1. xml 파일 불러오기
```python
with open(file_path) as f:
	xml = f.read()
```
위의 코드를 실행했을 때 다음과 같은 오류가 발생함
```
UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 43047: illegal multibyte sequence
```
다음과 같이 수정하면 오류가 발생하지 않음
```python
with open(file_path,'r',encoding='UTF8') as f:
	xml = f.read()
```
```python
tree = elemTree.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")
```
## 2. 원하는 부분 찾기
```python
sentences = tree.findall('./sentence') # 모든 sentence 찾기
sentence = sentences[0]
tok = sentence.find('./tok') # 첫 번째 tok 찾기
print(tok.tag)
print(tok.text)
```
```
tok
Hello
```