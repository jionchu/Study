# Logistic (regression) classification

## 1. Logistic classification
Classification 알고리즘 중에서 정확도가 높은 것으로 알려져 있다. 실제 문제에 바로 적용해 볼 수 있기 때문에 굉장히 중요한 알고리즘

### (Binary) Classification
둘 중 하나를 고르는 classification
- Spam Detection: Spam or Ham
- Facebook feed: show or hide
- Credit Card Fraudulent Transaction detection: legitimate/fraud
  - 평소에 신용카드를 사용하던 패턴을 분석하여 현재 사용하는 사람이 진짜인지 가짜인지 판단
  - 주식 시장에서 주식을 살지 말지 주식동향을 분석하여 판단

### 0, 1 encoding
- Spam Detection: Spam(1) or Ham(0)
- Facebook feed: show(1) or hide(0)
- Credit Card Fraudulent Transaction detection: legitimate(0) or fraud(1)

### Pass(1)/Fail(0) based on study hours
**binary classification model**  
Linear Regression으로도 할 수 있지 않을까?  
0부터 1까지의 결과값이 있을 때 0.5 이하는 Fail, 0.5 이상은 Pass로 하면 될 것 같다.  
⇒ 만약 50시간을 공부해서 pass했다면 그래프의 기울기가 작아지게 되면서 fail과 pass의 경계값 (0.5에 해당하는 값)이 커지게 되는 문제가 발생한다.  
⇒ 어떤 값들은 합격했는데도 불합격으로 인식된다.  
⇒ Classification에서는 0과 1 사이의 값이 나와야 하는데 H(x) = Wx +b의 경우에는 1보다 크거나 0보다 작은 값이 나올 수 있다.  
⇒ 0과 1 사이로 압축시켜주는 함수가 있으면 좋겠다!  
⇒ **sigmoid (logistic) function**  
- <img src="https://latex.codecogs.com/svg.latex?\;g(z)=\frac{1}{(1+e^{-z})}" title="g(z)"/>
- <img src="https://latex.codecogs.com/svg.latex?\;z=H(x)" title="z=H(x)"/>
sigmoid: curved in two directions, like the letter "S", or the Greek (sigma).

### Logistic hypothesis
<img src="https://latex.codecogs.com/svg.latex?\;H(X)=\frac{1}{(1+e^{-{W^T}X})}" title="Logistic hypothesis"/>

## 2. Cost function
logistic classification의 cost 함수는 linear regression의 cost 함수와 달리 구불구불해서 시작점에 따라 찾은 (local) 최소값이 다를 수 있다. global 최소값을 찾아야 함 → 이러한 함수는 사용할 수 없음

### New cost function for logistic
<img src="https://latex.codecogs.com/svg.latex?\;cost(W)=\frac{1}{m}\sum{c(H(x),y)}" title="Cost function"/>
<!-- <img src="https://latex.codecogs.com/svg.latex?\;c(H(x),y)={cases{-log(H(x))&:y=1#-log(1-H(x))&:y=0}" title="c(H(x),y)"/> -->
지수 함수로 인해 cost 함수가 구부러짐 → 구부러짐을 막기 위해 log 함수를 이용  
⇒ 두 개의 함수를 붙이면 linear regression cost function과 비슷한 모양이 된다.  
y: 실제값, H(X): 예측값 → y=1, H(x)=1 ⇒ cost(1)=0 / y=1, H(x)=0 ⇒ cost(0)=∞  
⇒ 프로그래밍 하기 편하게 수식을 조정한 것

### Minimize cost - Gradient descent algorithm
<img src="https://latex.codecogs.com/svg.latex?\;H(X)=\frac{1}{(1+e^{-{W^T}X})}" title="Logistic hypothesis"/>
<img src="https://latex.codecogs.com/svg.latex?\;cost(W)=-\frac{1}{m}\sum{ylog(H(x))+(1-y)log(1-H(x))}" title="Cost function"/>
<img src="https://latex.codecogs.com/svg.latex?\;W:=W-\alpha\frac{\partial}{\partial{W}}cost(W)" title="Gradient descent algorithm"/>