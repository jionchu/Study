## 1. Multi-Paradigm
### 숫자 리스트의 합을 구하는 코드 짜기
1. Procedural (Imperative)
- local 변수 사용
- for문이나 while문 많이 사용함
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

## 2. Java vs Python
1. Java
```java
int x = 3;
String s = "The answer is "+x;
```
```java
for (String w:words) {
    w = w.toUppercase();
    System.out.println(w);
}
```
```java
for (int i=2;i<9;i+=3)
    System.out.println(i);
```
```java
class Foo {
    static int count = 0;
    static int incCount() {
        count++;
        return count;
    }
}
```

2. Python
```python
x = 3
s = "The answer is "+str(x)
```
```python
for w in words:
    w = w.upper()
    print w
```
```python
for i in range(2,9,3):
    print i
```
```python
calss Foo:
    count=0
    @staticmethod
    def incCount(): # no self
        Foo.count += 1
        return Foo.count
```
