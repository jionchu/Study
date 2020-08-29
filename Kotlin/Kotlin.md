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

## 3. 함수
`fun` 키워드 뒤에 함수 이름이 오도록 한다. 그 다음 함수에 사용되는 입력 유형을 (있는 경우) 정의하고 함수에서 반환하는 출력 유형을 선언한다. 함수의 본문에서는 함수를 호출할 때 호출되는 표현식을 정의한다.
```java
fun generateAnswerString(): String {
    val answerString = if (count == 42) {
        "I have the answer."
    } else {
        "The answer eludes me."
    }

    return answerString
}
```
```java
val answerString = generateAnswerString()
```
아래와 같이 parameter를 입력으로 사용할 수 있다.
```java
fun generateAnswerString(countThreshold: Int): String {
    val answerString = if (count > countThreshold) {
        "I have the answer."
    } else {
        "The answer eludes me."
    }

    return answerString
}
```
```java
val answerString = generateAnswerString(42)
```

### 함수 선언 단순화
함수에 포함된 if-else 표현식의 결과를 직접 반환하여 로컬 변수 선언을 건너뛸 수 있다.
```java
fun generateAnswerString(countThreshold: Int): String {
    return if (count > countThreshold) {
        "I have the answer."
    } else {
        "The answer eludes me."
    }
}
```
반환 키워드를 할당 연산자로 바꿀 수도 있다.
```java
fun generateAnswerString(countThreshold: Int): String = if (count > countThreshold) {
    "I have the answer."
} else {
    "The answer eludes me."
}
```

### 익명 함수
모든 함수에 이름이 필요하지는 않다. 일부 함수는 입력과 출력에 의해 더 직접적으로 식별된다.
```java
val stringLengthFunc: (String) -> Int = { input ->
    input.length
}
```
위 예에서 `stringLengthFunc`는 `String`을 입력으로 사용하고 `String` 입력 길이를 `Int` 유형의 출력으로 반환하는 익명 함수 참조를 포함한다. 따라서 함수의 유형은 `(String) -> Int`로 표시된다. 하지만 이 코드는 함수를 호출하지 않는다. 함수의 결과를 가져오려면 이름이 지정된 함수처럼 호출해야 한다. 아래처럼 `stringLengthFunc`를 호출할 때 `String`을 input으로 넣어야 한다.
```java
val stringLengthFunc: (String) -> Int = { input ->
    input.length
}

val stringLength: Int = stringLengthFunc("Android")
```

### 고차(Higher-order) 함수
함수는 다른 함수를 인수로 취할 수 있다. 다른 함수를 인수로 사용하는 함수를 **고차 함수**라고 한다. 자바에서 콜백 인터페이스를 사용할 때와 동일한 방식으로 component 간에 통신하는 데 유용하다.

```java
fun stringMapper(str: String, mapper: (String) -> Int): Int {
    // Invoke function
    return mapper(str)
}
```
```java
stringMapper("Android", { input ->
    input.length
})
```
익명 함수가 함수에 정의된 마지막 매개변수인 경우 괄호 밖에서 함수를 전달할 수 있다.
```java
stringMapper("Android") { input ->
    input.length
}
```