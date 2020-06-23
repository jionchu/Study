# Methods for Transforming Grammars

제한 없이 작성된 **context free grammar**는 parsing 작업에서 시간이 오래 걸리거나 결과가 안나옴 (**비효율적**)  
→ 어떤 제한된 형태를 만족하는 동치의 문법으로 변형
→ 우측에 허용된 자유를 약간 희생하여 큰 효과를 얻게 됨

### Simplification
- 바람직하지 않은 생성규칙들을 제거하는 것
- 생성규칙의 수를 반드시 감소하는 것을 의미하지는 않음

## 1. Removing Useless Productions
### Useless Productions
- never terminate (문장에 변수가 계속 존재하게 되는 rule)
- not reachable from S
- 문장을 유도하는 과정에서 절대 사용되지 않는 rule들을 말한다.
- x의 모든 변수들이 useful하다면 A → x도 useful하다.

### 1) never terminate
#### ㄱ. find all variables that produce strings with only terminals
1. 직접적으로 terminal에 도달하는 변수 추가
2. 간접적으로 terminal에 도달하는 변수 추가 (ex. S → A → a)

#### ㄴ. keep only the variables that produce terminal symbols
terminal에 도달하는 변수 집합에 포함되지 않는 것은 삭제  
해당 변수를 포함하는 것들도 제거한다.

### 2) not reachable
#### ㄱ. find all variable 
dependency graph 이용

#### ㄴ. keep only the variables reachable from S
도달할 수 없는 변수 제거

## 2. Removing Nullable Variables
효율적인 결과를 위해서 빈 string은 제거 
1. **λ-production**
  - 빈 문자열을 바로 찾는 경우
  - A → λ
2. **Nullable Variable**
  - 유도해나가야 빈 문자열이 나오는 경우
  - A ⇒ ... ⇒ λ

빈 문자열에 영향받는 rule들을 변형한 후 빈 문자열을 삭제해야 함

- L-{λ}에 속해있는 경우가 아닌 경우에만 삭제 가능하다.
- 모든 nullable variable들을 먼저 찾아야한다.
- Original production(without λ, 기존에 있던 rule) + productions with nullable variables replaced by λ (all combination, λ의 영향을 받아 새롭게 추가된 것)

## 3. Removing Unit Productions
Unit Production: A → B

- A → A: 자기 자신으로 치환되는 경우에는 즉시 삭제 가능
- 다른 곳에 영향을 줘서 unit production이 나오는지 확인
- dependency graph 그려보기

### 1) Example
- S → Aa | B
- B → A | bb
- A → a | bc | B

#### Step 1. Unit production closure
- S → B → A
- B → A
- A → B

#### Step 2
원래 Unit Production이 아닌 것들
- S → Aa
- B → bb
- A → a | bc

#### Step 3
Apply Unit production closure  
Step 1에서 구한
- S → B | A
- B → A
- A → B
의 각 unit production을 step2의 rule들로 치환한다.
- S → a | bc | bb
- B → a | bc
- A → bb

#### Step 4. Final Result
step2와 step3 결합
- S → Aa | a | bc | bb
- B → bb | a | bc
- A → bb | a | bc

## 3. Remove All
- **Step 1**: Remove Nullable Variables
- **Step 2**: Remove Unit-Productions
- **Step 3**: Remove Useless Variables

**Order is important!**