## 1. Data type

### 주요 데이터 타입
- string
- number
- boolean
- null
- undefined
- symbol

### 숫자 vs 문자열
- 데이터 타입에 따라 결과가 달라짐
- ex) 1+1 => 2 / "1"+"1" => 11

### Number
- 산술 연산자 4개
- +, -, *, /

### BigInt

### String
- 따옴표 안에 넣어 표현
```javascript
var name = " jionchu"
```
- length: 문자열 길이 출력
```javascript
console.log(name.length)
```
```
8
```
- toUpperCase: 소문자 -> 대문자 변환
```javascript
console.log(name.toUpperCase())
```
```
 JIONCHU
```
- indexOf
```javascript
console.log(name.indexOf('c'))
```
```
5
```
- trim: 문자열 좌우측의 공백 없애기
```javascript
console.log(name.trim)
```
```
jionchu
```