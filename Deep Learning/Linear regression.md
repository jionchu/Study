# 02. Linear Regression

## 1. Hypothesis & Cost of Linear Regression
### (Linear) Hypothesis  
- <img src="https://latex.codecogs.com/svg.latex?\;H(x)=W(x)+b" title="hypothesis" />
- 실제 데이터에 맞는 선을 찾는 것

### Cost (Lost) function
- <img src="https://latex.codecogs.com/svg.latex?\;cost(W,b)=\frac{1}{m}\sum_{i=1}^{m}(H(x^{(i)})-y^{(i)})^2" title="cost_function" />
- 가설과 실제 데이터의 차이
- cost 값이 작을수록 좋은 가설
- cost 값이 가장 작은 W와 b를 찾는 과정을 __학습__ 이라고 한다.
