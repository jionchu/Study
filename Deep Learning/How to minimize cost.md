# 03. How to minimize cost
cost function을 어떻게 minimize하여 최종적으로 linear regression 학습을 완성시키는가

### Simplified hypothesis
계산의 편의를 위해 식을 간략히 바꿈
- <img src="https://latex.codecogs.com/svg.latex?\;H(x)=Wx" title="hypothesis" />
- <img src="https://latex.codecogs.com/svg.latex?\;cost(W)=\frac{1}{m}\sum_{i=1}^{m}(H(x^{(i)})-y^{(i)})^2" title="cost_function" />
ex) x =1, Y=1 / x=2, Y=2 / x=3, Y=3  
W=1, cost(W)=0  
W=0, cost(W)=4.67  
W=2, cost(W)=4.67  
=> W 값의 변화에 따라 cost 값이 어떻게 변화하는지 그래프 그려보기  
![cost graph](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/cost-graph.png)  
=> cost 값이 가장 작은 W 알아내기

## 1. Gradient descent algorithm
- 경사를 따라 내려가는 알고리즘
- Minimize cost function
- Gradient descent is used many minimization problems
- For a given cost function, cost(W,b), it will find W, b to minimize cost
- It can be applied to more general function: cost (W1, W2, ...)
- 많은 값들이 있는 cost function도 minimize할 수 있는 알고리즘

### How it works?
- Start with initial guesses
- Start at 0,0 (or any other value)
- Keeping changing W and b a little bit to try and reduce cost(W,b)
- 항상 최저점에 도달할 수 있다는 것이 이 알고리즘의 장점
- 경사도는 미분을 이용하여 구함
- <img src="https://latex.codecogs.com/svg.latex?\;W:=W-\alpha{{\partial}\over{\partial{W}}}{cost(W)}" title="partial deirivative" />
- cost 함수를 특정 좌표에서 미분한 값이 음수인 경우 W-(음수)가 되어 W 값은 커짐
- <img src="https://latex.codecogs.com/svg.latex?\;W:=W-\alpha{{\partial}\over{\partial{W}}}\frac{1}{2m}\sum_{i=1}^{m}(Wx^{(i)}-y^{(i)})^2" title="partial deirivative" /> -> 미분했을 때 깔끔하게 하기 위해서 1/2 추가
- <img src="https://latex.codecogs.com/svg.latex?\;W:=W-\alpha\frac{1}{2m}\sum_{i=1}^{m}2(Wx^{(i)}-y^{(i)})x^{(i)}" title="partial deirivative" />
- <img src="https://latex.codecogs.com/svg.latex?\;W:=W-\alpha\frac{1}{m}\sum_{i=1}^{m}(Wx^{(i)}-y^{(i)})x^{(i)}" title="partial deirivative" />
- 위의 식을 여러 번 실행시키면서 W 값이 변하면 최종적으로 cost를 minimize하는 W 값이 자동으로 구해짐

### 주의할 점
- Where you start can determine which minimum you end up

## 2. Convex function
### non-convex function
![non-convex function](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/non-convex-function.png)  
- cost function이 convex function이 아닌 경우 시작점에 따라 결과값이 다르게 나옴 => 알고리즘이 제대로 동작하지 않음  

### convex function
![convex function](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/convex-function.png)
- convex function의 경우 Gradient decent algorithm이 항상 답을 찾음
- Linear regression을 적용하기 전에 cost function이 convex function 모양인지 확인해야 함