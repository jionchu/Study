# Methods for Transforming Grammars

제한 없이 작성된 context free grammar는 parsing 작업에서 시간이 오래 걸리거나 결과가 안나옴 (비효율적)  
→ 어떤 제한된 형태를 만족하는 동치의 문법으로 변형
→ 우측에 허용된 자유를 약간 희생하여 큰 효과를 얻게 됨

### Simplification
- 바람직하지 않은 생성규칙들을 제거하는 것
- 생성규칙의 수를 반드시 감소하는 것을 의미하지는 않음

## 1. A Useful Substitution Rule

## 2. Removing Useless Productions
### Useless Productions
- never terminate
- not reachable from S

### 1) never terminate
#### ㄱ. find all variables that produce strings with only terminals
1. 직접적으로 terminal에 도달하는 변수 추가
2. 간접적으로 terminal에 도달하는 변수 추가 (ex. S → A → a)

#### ㄴ. keep only the variables that produce terminal symbols
terminal에 도달하는 변수 집합에 포함되지 않는 것은 삭제

### 2) not reachable
#### ㄱ. find all variable 
- dependency graph 이용

#### ㄴ. keep only the variables reachable from S
도달할 수 없는 변수 제거

## 3. Removing Nullable Variables
효율적인 결과를 위해서 빈 string은 제거 
1. 빈 문자열을 바로 찾는 경우
2. 유도해나가야 빈 문자열이 나오는 경우

빈 문자열에 영향받는 rule들을 변형한 후 빈 문자열을 삭제해야 함
