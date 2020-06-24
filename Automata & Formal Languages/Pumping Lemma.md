# Pumping Lemma

## 1. Pumping Lemma
context-free language가 **infinite**라는 것은 어딘가에 loop가 있다는 뜻 → pumping lemma로 증명

어떠한 positive integer m에 대하여 길이가 m 이상인 L에 속하는 문자열 w는 다음과 같이 분할할 수 있다.
- w = uvxyz
- **|vxy| ≤ m**
- **|vy| ≥ 1** (v 또는 y가 빈 문자열일 수 있으나 둘 다 빈 문자열이면 안됨. pumping했을 때 길이가 늘어나야 하기 때문)
- uvⁿxyⁿz ∈ L
- for all n = 0,1,2,...

즉, 어떠한 문자열이 context free language에 속한다면 반드시 uvxyz의 형태로 표시되며 uvⁿxyⁿz도 이 언어에 항상 속한다.

## 2. Applications of the Pumping Lemma
### Context free language가 아닌 언어군이 존재함을 증명
L = {aⁿbⁿcⁿ: n≥0}
1. context free language라고 가정
2. pumping lemma 만족 X
3. 모순 → context free language가 아님 증명
