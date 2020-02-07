# Multi-variable linear regression
입력값이 여러개인 linear regression

## 1. Multi-variable linear regression

ex) regression using three inputs (x1, x2, x3)

|x1 (quiz1)|x2 (quiz2)|x3 (midterm1)|Y (final)|
|:--------:|:--------:|:-----------:|:-------:|
|73|80|75|152|
|93|88|93|185|
|89|91|90|180|
|96|98|100|196|
|73|66|70|142|

위와 같이 입력값이 여러 개인 linear regression이 있을 때 hypothesis와 cost function은 다음과 같다.  
<img src="https://latex.codecogs.com/svg.latex?\;H(x_1,x_2,x_3)=w_1x_1+w_2x_2+w_3x_3+b" title="hypothesis" />  
<img src="https://latex.codecogs.com/svg.latex?\;cost(W,b)=\frac{1}{m}\sum_{i=1}^{m}(H(x_1^{(i)},x_2^{(i)},x_3^{(i)})-y^{(i)})^2" title="cost_function" />  

input이 더 많아지면 다음과 같이 표현한다.  
<img src="https://latex.codecogs.com/svg.latex?\;H(x_1,x_2,x_3,...,x_n)=w_1x_1+w_2x_2+w_3x_3+...+w_nx_n+b" title="hypothesis" />  
많아질수록 일일이 수식을 늘려줘야 하는게 불편 -> Matrix 이용!

### 참고) Matrix의 곱셈

### Hypothesis using matrix
matrix를 이용하여 우리의 hypothesis를 간단하게 표현할 수 있다.
<img src="https://latex.codecogs.com/svg.latex?\;w_1x_1+w_2x_2+w_3x_3+...+w_nx_n" title="hypothesis" />  
<img src="https://latex.codecogs.com/svg.latex?\;w_1x_1+w_2x_2+w_3x_3+...+w_nx_n" title="hypothesis" />  


### instance가 많은 경우
하나의 데이터 묶음을 instance라고 한다. 위의 예시에서는 (x1:73, x2:80, x3:75) 한 줄이 하나의 instance이다.  
