# Multinomial classification

## 1. Multinomial classification
여러 개의 클래스가 있을 때 그것을 예측하는 것  
**softmax classification**: multinomial classification 중에서 가장 많이 쓰이는 것  
![logistic regression](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/logistic_regression.png)

logistic regression을 학습시킨다는 것은 두 집단을 구분하는 선을 찾는 것이다. 만약 세 집단이 있다면 구분하는 선을 어떻게 찾을 것인가?  

![multinomial classification](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/multinomial_classification.png)  
![multi binary classification](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/multi_binary_classification.png)  
세 개의 각각 다른 binary classification을 이용해서 구현 가능  

![multinomial matrix1](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/multinomial_matrix1.png) 
![multinomial graph1](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/multinomial_graph1.png)  
하지만 세 개를 독립적으로 구현하는 것은 복잡하므로 하나로 합친다.  

![multinomial matrix2](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/multinomial_matrix2.png)  
이렇게 하면 하나의 classification이 오른쪽 그림과 같이 독립된 classification처럼 동작하게 된다.  

## 2. ONE-HOT ENCODING
확률이 제일 큰 값을 1로 만들고 나머지를 0으로 만든다. tensorflow에서는 argmax를 이용한다.  

### example
1. logistic classifier를 통해 점수 y 값을 구한다.
2. softmax를 이용하여 확률을 계산한다. (0과 1 사이의 값, 전체 합 = 1)
3. one-hot encoding을 이용하여 확률이 가장 큰 것을 찾는다.

![logistic classification](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/one_hot_logistic_classification.png)
![softmax](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/one_hot_softmax.png)  

## 3. Cross entropy
### Cross entropy cost function
s(y)는 예측해낸 값(<img src="https://latex.codecogs.com/svg.latex?\;\bar{Y}" title="y hat"/>), L은 실제 값(정답), 앞에서는 Y라고 표현함  
예측값(s(y))과 실제 값(L)의 차이를 cross entropy라는 함수를 이용해서 구함
<img src="https://latex.codecogs.com/svg.latex?\;D(S,L)=-\sum_{i}{L_i}log(S_i)" title="cross entropy function"/>  

예측값과 정답이 같을 때 cost는 0이고, 예측값과 정답이 다를 때 cost는 ∞이다.  

### Logistic cost vs Cross entropy
[Logistic regression (classification)](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/Logistic%20regression%20(classification).md)에서 말한 cost function이 사실상 cross entropy function이었다.  
<img src="https://latex.codecogs.com/svg.latex?\;C(H(x),y)=\sum{ylog(H(x))+(1-y)log(1-H(x))}=D(S,L)" title="Cost function"/>  

위의 식은 training set이 한개인 경우이고 여러 개의 training set이 있을 때의 cross entropy cost function은 다음과 같다. (n개의 training set이 있을 때)  
<img src="https://latex.codecogs.com/svg.latex?\;L=\frac{1}{n}\sum_{i}^{n-1}D(S(WX_i+b),L_i)" title="cross entropy function"/>  

### Minimize cost
마찬가지로 Gradient descent 알고리즘을 사용하여 cost 값을 최소화하는 W 값을 찾아낸다.