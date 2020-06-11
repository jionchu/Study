# Nondeterministic Pushdown Automata

## 1. Pushdown Automata - PDA
개수 비교 등의 추가적인 정보를 저장하기 위해 **stack** 이용

## 2. Non-Determinism
- multi choice 가능
- transition 없을 수 있음
- lambda transition 가능

### 1) Accepted by the NPDA
A string is accepted if there is a computation such that
- All the input is consumed (모든 input을 다 읽어야 함)
- The last state is a final state (final state에 도달해야 함)
- 가능한 transition이 없는 경우 reject

computation이 끝난 후 stack에 남아 있는 content들은 상관하지 않음  
