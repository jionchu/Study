# Programing Paradigm

### 숫자 리스트의 합을 구하는 코드 짜기
1. Procedural (Imperative)
```python
myList = [1,2,3,4,5]
def addList(myList):
    sum = 0
    for x in myList:
        sum += x

addList(myList)
```
2. Functional
```python
myList=[1,2,3,4,5]
def add(x,y):
    return (x+y)

sum = reduce(add,myList)
print sum
```

3. Object-oriented
```python
myList = [1,2,3,4,5]
class AddList:
    def __init__(self,myList):
        self.myList = myList
    def addList(self):
        return reduce(add,myList)

x = AddList(myList)
x.addList()
```
