# Parsing and Ambiguity

## 1. Ambiguity
- L(G)에 속하는 문자열 w를 만드는 derivation tree가 2개 이상 존재하는 context-free grammar

#### why do we care about ambiguity?
![ambiguity](https://github.com/jionchu/TIL/blob/master/Automata%20&%20Formal%20Languages/images/ambiguity.PNG)  
=> 결과가 달라지게 되어 위험함

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

## 2. Parsing
### 1) Parser
Program --input--> Compiler --output--> Machine code  

- Compiler의 구성은 다음과 같다.

Lexical analyzer -> Parser  
=> Program --input--> Lexical analyzer -> Parser --output--> Machine code  

- Parser knows the grammar of the programming language
- Parser finds the derivation fo a particular input

### 2) Parsing
- L(G)에 속하는 w에 대해 일련의 생성규칙을 발견하는 과정

### 3) s-grammar (simple gramamr)
- faster algorithms for specialized grammars
- In the exhaustive search parsing, there is only one choice in each phase
- Time for a phase: 1
- Total time for parsing string: W (각 심볼에 대해 1번만 탐색하면 되므로 문자열의 길이만큼 시간이 걸림)

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
