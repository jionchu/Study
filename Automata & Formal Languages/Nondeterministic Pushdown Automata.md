# Nondeterministic Pushdown Automata

## 1. Pushdown Automata - PDA
개수 비교 등의 추가적인 정보를 저장하기 위해 **stack** 이용
- context free grammar로 만들어지는 automata
- initial state의 stack에는 bottom symbol($)만 들어있음
- *a, b → c* (Replace)
  - a를 읽고 b를 pop하고 c를 push
- *a, λ → c* (Push)
  - 아무것도 pop하지 않음
- *a, b → λ* (Pop)
  - 아무것도 push하지 않음
- *a, λ → λ* (No change)
  - 아무 변화 없음

## 2. Non-Determinism - NPDA
- multi choice 가능 (a, b → c를 하고 q1로 갈 수도, q2로 갈 수도 있음)
- transition 없을 수 있음
- λ-transition 가능

### 1) Accepted by the NPDA
A string is accepted if there is a computation such that
- All the input is consumed (모든 input을 다 읽어야 함)
- The last state is a final state (final state에 도달해야 함)
- 가능한 transition이 없는 경우 reject

computation이 끝난 후 stack에 남아 있는 content들은 상관하지 않음  

### Pushing Strings
여러 개의 symbol을 한 번에 push할 수 있음  
문자열의 시작이 stack의 가장 위로 올라감

## 3. Formal Definition of NPDA
M = (Q,Σ,Γ,δ,q0,z,F)
- **Q**: States
- **Σ**: Input alphabet
- **Γ**: Stack alphabet (finite automata랑 다른 점)
- **δ**: Transition function
- **q0**: Initial state
- **z**: Stack start symbol (finite automata랑 다른 점)
- **F**: Final state

### 1) Transition function
δ : Q x (Σ ∪ {λ}) x Γ → finite subsets of Q x Γ*
- δ(q1,a,b) = {(q2,w)} : w는 push할 string
- δ(q1,a,b) = {(q2,w), (q3,w)}

nondeterministic이기 때문에 여러 길이 존재 → transition function은 집합으로 표현한다.

### 2) Instantaneous Description (순간적 묘사)
NPDA에서는 현재 state가 어디인지만 알 수 있음  
앞으로 읽을 string들의 정보를 알고 싶어서 instantaneous description을 추가함

(q, u, s)
- **q**: Current state
- **u**: Remaining input
- **s**: Current stack contents

#### ㄱ. Move
(q₁,aw,bx) ├ (q₂,w,yx) iff (q₂,y)∈δ(q₁,a,b) → (q₁,a,b) 상태에서 a를 읽고 b를 pop하고 y를 push함

## 4. Formal Definition of L(NPDA)
NPDA M에 의해 인식되는 language  
L(M) = {w: (q0,w,s) ├* (qf,λ,s')}
- (q0,w,s) ← **Initial state**
- (qf,λ,s') ← **Final state** (stack에는 뭐가 남아있든 상관 없음)

### 1) NPDAs Accept Context-Free Languages
#### Theorem
Context-Free Languages (Grammars) = Languages Accepted by NPDAs

#### Proof - Step 1: ⊆
모든 context-free grammar는 NPDA로 변환 가능하다.

#### Proof - Step 2: ⊇
모든 NPDA는 context-free grammar로 변환 가능하다.

#### ㄱ. Proof: Converting CFGs to NPDAs
Basic idea
- NPDA carrying out a leftmost derivation of strings
- 모든 context-free grammar는 **Greibach Normal Form**(GNF)로 변환 가능
  - 오른쪽의 변수들은 **stack**에 push
  - 왼쪽의 terminal들은 **input read**
- A → ax
  - A: stack에서 pop
  - a: input read
  - x: stack에 push
