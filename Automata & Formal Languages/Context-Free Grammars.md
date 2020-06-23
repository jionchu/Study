# Context-Free Grammars

## 1. Context-Free Languages
### 1) Context-Free Languages
- 임시저장소 **stack**이 추가로 있음
- **Context-Free Grammar**에 의해 생성되는 string들의 집합
- **Pushdown Automata**
- 현재 쓰이는 대부분의 프로그램 작성 언어의 문법 구조
- Regular language가 아닌 것도 표현 가능
- ex) {a^nb^n}, {ww^R} → pumping lemma를 이용해 regular language가 아님을 증명했음

### 2) Context-Free Grammars
*어떠한 language를 만들어내는 context free grammar는 다양하게 존재할 수 있음*  

G = (V,T,S,P)  
- V : Variables
- T : Terminal symbols
- S : Start variable
- P : Productions of the form
  - Regular language보다 제약이 적어진 형태
  - Regular language는 우측에 변수가 1개만 있어야 하고 맨 오른쪽에 있거나(right-linear grammar) 맨 왼쪽에 있어야만(left-linear grammar) 했지만 Context-Free Grammar는 개수, 위치 **제약 없음**
  - A → x  
  where A ∈ V and x ∈ (V ∪ T)*  
  (x is string of variables and terminals)

ex) G = ({A}, {x, y, z}, S, {A → x, A → y})

#### ㄱ. example 1
A context-free grammar G:
- S → aSb (변수가 가운데에 있으므로 regular X)
- S → λ

*A derivation*:  
S ⇒ aSb ⇒ aaSbb ⇒ aabb

*Another derivation*:  
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb

L(G) = {a^nb^n: n≥0} ⇒ 빈 string도 포함

## 2. Derivation Order
- **Leftmost Derivation**: 왼쪽에 있는 변수부터 치환해나감
- **Rightmost Derivation**: 오른쪽에 있는 변수부터 치환해나감

### 1) Example 1
1. S → AB
2. A → aaA
3. A → λ
4. B → Bb
5. B → λ

#### ㄱ. Leftmost Derivation
S ⇒ AB ⇒ aaAB ⇒ aaB ⇒ aaBb ⇒ aab

#### ㄴ. Rightmost Derivation
S ⇒ AB ⇒ ABb ⇒ Ab ⇒ aaAb ⇒ aab

### 2) Example 2
1. S → aAB
2. A → bBb
3. B → A | λ

#### ㄱ. Leftmost Derivation
S ⇒ aAB ⇒ abBbB ⇒ abAbB ⇒ abbBbbB ⇒ abbbbB ⇒ abbbb

#### ㄴ. Rightmost Derivation
S ⇒ aAB ⇒ aA ⇒ abBb ⇒ abAb ⇒ abbBbb ⇒ abbbb

## 3. Derivation Trees
- 더 이상 치환할 수 없는 단말노드들을 연결해서 sentence를 만듦 (깊이 우선 탐색)
- **sometimes** derivation order doesn't matter
- leftmost derivation과 rightmost derivation의 결과 derivation tree가 동일하게 나올 수도 있다.
- 여러 개의 derivation tree가 나오는 경우 : **ambiguous**

1. S → AB
2. A → aaA | λ
4. B → Bb | λ

![derivation tree](https://github.com/jionchu/TIL/blob/master/Automata%20&%20Formal%20Languages/images/derivation_tree.PNG)  

## 4. Partial Derivation Trees
- 단말 노드(child가 없는 노드)가 변수인 것을 포함하고 있는 형태의 tree
- Partial derivation tree에서 단말 노드들을 연결해서 만든 sentence는 **sentential form**이 된다.  

1. S → AB
2. A → aaA | λ
4. B → Bb | λ

#### ㄱ. S ⇒ AB
![partial derivation tree](https://github.com/jionchu/TIL/blob/master/Automata%20&%20Formal%20Languages/images/partial_derivation_tree_ex1.PNG)  

#### ㄴ. S ⇒ AB ⇒ aaAB
![partial derivation tree](https://github.com/jionchu/TIL/blob/master/Automata%20&%20Formal%20Languages/images/partial_derivation_tree_ex2.PNG)  
