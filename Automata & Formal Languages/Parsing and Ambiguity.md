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
