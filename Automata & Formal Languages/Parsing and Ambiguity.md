# Parsing and Ambiguity

## 1. Ambiguity
- L(G)에 속하는 문자열 w를 만드는 derivation tree가 2개 이상 존재하는 context-free grammar
- leftmost (or rightmost) derivation이 2개 이상 존재하는 것
- ambiguous 증명: derivation tree가 2개 이상 나타나는 string 찾기

#### why do we care about ambiguity?
![ambiguity](https://github.com/jionchu/TIL/blob/master/Automata%20&%20Formal%20Languages/images/ambiguity.PNG)  
⇒ 결과가 달라지게 되어 위험함

### 1) Non-ambiguous
- ambiguity is **bad** for programming languages
- ambiguity를 제거해야 함

E → E+E | E*E | (E) | a  

\* 위의 grammar를 아래의 grammar로 수정한다.  

E → E+T  
E → T  
T → T*F  
T → F  
F → (E)  
F → a  

### 2) Inherent Ambiguity
CFL (Context-Free Language) L에 대해
- non-ambiguous 문법 G가 존재한다면 L은 **unambiguous**
- G가 존재하지 않는다면 L은 **inherently ambiguous** (non-ambiguous grammar로 고치지 못함)
- 증명은 배우지 않음

## 2. Parsing
### 1) Parser
**Program** --input--> **Compiler** --output--> **Machine code**  

- Compiler의 구성은 다음과 같다.

Lexical analyzer (어휘분석, 키워드, 변수명이 숫자로 시작하지는지 등 → *regular language로 커버 가능*) --> Parser (if, while 블록 검사, 괄호쌍 → sentence가 제대로 유도되는지)  
⇒ **Program** --input--> **Lexical analyzer** -> **Parser** --output--> **Machine code**  

- Parser knows the grammar of the programming language (내부적으로 grammar를 가지고 있어야 함)
- Parser finds the derivation fo a particular input

### 2) Parsing
- L(G)에 속하는 w에 대해 일련의 생성규칙을 발견하는 과정
- parser가 가지고 있는 grammar에 의해 input string이 유도과정을 통해 산출물을 내주는지 확인하는 과정

#### ㄱ. exhaustive search (top-down parsing)
input이 들어온 후
1. input string이 절대 나올 수 없는 규칙 제외
2. 각각을 치환하고 절대 나올 수 없는 규칙 제외 반복
3. 원하는 결과 찾기

하지만 절대 이 grammar로 나올 수 없는 sentence를 input으로 넣으면?  
⇒ 무한 loop에서 빠져나오지 못함 ⇒ 중간에 중지시켜야 함

⇒ 길이로 판단하기 위해 lambda transition과 unit production을 삭제한다. (탐색이 계속되어도 길이가 길어지지 않기 때문) ⇒ time completity 최대 **2|w|** (**1w**: 변수 치환으로 길이가 늘어나는 단계, **1w**: 변수를 terminal로 변환하는 단계)  
⇒ 효과적으로 parsing할 수 있음

#### ㄴ. Time complexity of exhaustive search
grammar에 k개의 production rule이 있을 때 w의 derivation을 찾기 위해서는
- Time for *phase 1*: k possible derivation
- Time for *phase 2*: k^2 possible derivation
- Time for *phase 2|w|*: k^2|w| possible derivation (길이가 w가 될 때까지)

string w를 찾기 위한 total time은
- k + k^2 + ... + k^2|w|
- **Extremely bad!!**

### 3) s-grammar (simple gramamr)
- faster algorithms for specialized grammars
- In the exhaustive search parsing, there is only one choice in each phase
- Time for a phase: 1
- Total time for parsing string: |W| (각 심볼에 대해 1번만 탐색하면 되므로 문자열의 길이만큼 시간이 걸림)

A → ax  
pair (A, a) appears once

#### ㄱ. S-grammar example
- S → aS
- S → bSS
- S → c

Each string has a **unique** derivation  
S => aS => abSS => abcS => abcc

#### ㄴ. not S-grammar example
- S → aS | bSS | aSS | c

pair (S, a) appears **twice**
- S → aS
- S → aSS

### 4) general context-free grammars
- There exists a parsing algorithm that parses a string W in time |W|^3

## 3. Programming Language
- Formal Language: one of the most important uses
- Regular Language: recognition of certain simple patterns. ex) 변수 이름이 숫자로 시작하지 않게 확인
- Context-Free Languages: more complicated aspects. ex) 괄호 쌍 확인

### 1) Context-Free Grammar & PL
comvention for specifying grammars for PL: **Backus-Naur Form** (Context-Free Grammar 표현 방식) 

#### ㄱ. example 1
\<expression> ::= \<term> | \<expression> + \<term>  
\<term> ::= \<factor> | \<term> * \<factor>  

S → aA => \<S> ::= a\<A>

#### ㄴ. example 2
**s-grammar**: easily/efficiently parsed (due to **keywords**)  
\<if_stmt> ::= if \<expression> \<then_cause> \<else_cause>  
→ **LL/LR grammars**
