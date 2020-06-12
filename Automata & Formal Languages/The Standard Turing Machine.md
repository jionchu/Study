# The Standard Turing Machine

## 1. Definition
Context-Free Languages에서 사용하는 stack도 부족 → 유연한 저장구조가 필요함  
=> **Tape**를 사용하는 Turing Machine

- **Tape**: infinite length
- **Control Unit**: symbol을 read, write하고 Read-Write head를 움직이는 것을 제어함
- input string이 tape에 입력되면 read-write head가 이동함

### 1) The Input String
- 초기에 head는 input string의 제일 왼쪽을 가리킴
- 빈 cell들은 blank symbol(◇)로 표현

### 2) States & Transtions
a → b,L  
- a: Read
- b: Write
- L: Move Left / R: Move Right

### 3) Determinism
- 어떠한 symbol을 읽었을 때 갈 수 있는 길은 단 1개뿐
- lambda transition도 존재하지 않음 (blank를 읽는 것과는 다름)

### 4) Partial Transition Functionn
어떠한 state에서 모든 input string symbol들에 대한 transition이 정해져 있어야 하는 것은 아님  
하지만 read한 input symbol에 대해서는 가능한 transition이 존재해야 함  
가능한 transition이 존재하지 않는 경우 => **HALT** (시스템 중지)  

### 5) Final States
- Final states have no outgoing transitions
- In a final state the machine halts
- final state에 도달하면 시스템이 중지됨

### 6) Acceptance
- Accept Input: If machine halts in a **final state**
- Reject Input: If machine halts in a **non-final state** or If machine enters an **infinite loop**
