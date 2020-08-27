# Kotlin

## 1. 변수 선언

두 keyword(val, var)를 사용하여 변수 선언
- **val** : 값이 변경되지 않는 변수에 사용. val을 사용하여 선언된 변수에 값을 재할당할 수 없음
- **var** : 값이 변경될 수 있는 변수에 var 사용

```java
var count: Int = 10
count = 15
```
```java
val languageName: String = "Kotlin"
```

### Type inference
- 변수 초기 값을 할당할 때 Kotlin 컴파일러는 할당된 값의 유형을 기반으로 유형을 추론할 수 있음
- Kotlin은 정적으로 입력되는 언어이므로 컴파일 시에 유형이 결정되고 절대 변경되지 않음
- 간결성과 유형 안전성을 보장함

```java
val languageName = "Kotlin"
val upperCaseName = languageName.toUpperCase()

// Fails to compile
languageName.inc()
```
String class의 함수가 아닌 것을 호출할 수 없음 (inc()는 Int 연산자 함수)

### Null safety
- Kotlin 변수는 null 값을 가질 수 없음
```java
// Fails to compile
val languageName: String = null
```
null 값을 포함하는 변수는 *nullable* 유형이어야 함. `?`을 변수 type의 접미사로 지정하여 변수를 nullable로 지정할 수 있음

```java
val languageName: String? = null
```
nullable 변수는 신중하게 처리하지 않으면 NullPointerException이 발생할 수 있다.  

Kotlin은 nullable 변수로 안전하게 작업하기 위한 많은 메커니즘을 제공한다.

## 2. 조건문
### if-else문
```java
if (count == 42) {
    println("I have the answer.")
} else if (count > 35) {
    println("The answer is close.")
} else {
    println("The answer eludes me.")
}
```
반복을 피하기 위해 다음과 같이 작성할 수 있음
```java
val answerString: String = if (count == 42) {
    "I have the answer."
} else if (count > 35) {
    "The answer is close."
} else {
    "The answer eludes me."
}

println(answerString)
```
### when
각 분기는 조건, 화살표(`->`) 및 결과로 표시됨
```java
val answerString = when {
    count == 42 -> "I have the answer."
    count > 35 -> "The answer is close."
    else -> "The answer eludes me."
}
println(answerString)
```

### smart casting
safe-call operator나 not-null assertion을 사용하는 대신 조건문을 사용하여 변수에 null 값이 있는지 확인할 수 있다.
```java
val languageName: String? = null
if (languageName != null) {
    // No need to write languageName?.toUpperCase()
    println(languageName.toUpperCase())
}
```
