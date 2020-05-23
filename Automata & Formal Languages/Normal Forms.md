# Normal Forms

## 1. Chomsky Normal Form
변수가 terminal 혹은 두 개의 변수로 mapping 되는 것
- A → BC
- A → a

- Chomsky normal forms are good for parsing and proving theorems
- It is very easy to find the Chomsky normal form of any context-free grammar

## 2. Greibach Normal Form
왼쪽에 symbol이 나오고 오른쪽에 변수가 나오는 것 (변수 개수 상관 없음)
- A → aV1V2...Vk

제일 왼쪽 symbol 이외의 symbol들은 전부 변수로 대체  
일반화시키기 어려움

- very good for parsing
- It is hard to find the Greibach normal form of any context-free grammar

## 3. Membership Algorithm
문자열이 grammar로 유도될 수 있는지 찾는 알고리즘