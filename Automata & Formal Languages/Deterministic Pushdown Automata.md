# Deterministic Pushdown Automata

## 1. Deterministic Pushdown Automata - DPDA
- 모든 symbol의 길이 정해져있을 필요는 X
- but, 길은 하나만 있어야 함

### Allowed
- 하나의 symbol을 읽어도 pop해야 하는 대상이 다르면 multi choice 아님
  - a,b → w1
  - a,c → w2
- 빈 문자열로 이동 가능하지만 pop할 대상이 있어야 함
  - λ,b → w

### Not allowed
- 읽어들이는 symbol과 pop하는 대상이 동일한 경우 → multi choice ⇒ 허용 X
  - a,b → w1
  - a,b → w2
- 읽어들이는 symbol이 달라도 pop하는 대상이 동일하면 안됨
  - λ,b → w1
  - a,b → w2
- 빈 문자열을 읽어들이면서 pop 하는 대상이 없는 경우
  - λ,λ → λ

## 2. NPDA & DPDA
NPDA(Non-DPDA)가 DPDA보다 power가 강력하다. (=인식할 수 있는 언어군이 크다. DPDA가 인식하는 언어군 포함)

DPDA로 인식할 수 없는 context-free language(NPDA로 인식 가능)가 존재함을 보여 증명

- L = {aⁿbⁿ} ∪ {aⁿb²ⁿ}
Proof: L을 인식하는 오토마타가 DPDA라고 가정하고 모순임을 증명한다.

## 3. Grammars for DCFL (Deterministic context-free languages)
### Importance of DCFL
DPDA는 multi choice가 아니기 때문에 **no backtracking** → give us an **efficient parser** (parsing 효과적)

- S-Grammar
  - 변수와 symbol의 pair가 하나 뿐
  - S → aS | bSS | c
- LL Grammar
  - input scanned left to right
  - leftmost derivation
  - LL(k) - k: 한 번에 읽을 symbol의 개수
  - 여러 개의 input을 한번에 읽을 때 명확함
  - S → aS | bSS | c
- LR Grammar
  - more general deterministic grammar
  - S → SS | aSb | ab