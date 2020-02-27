# Backpropagation

## 1. 딥러닝으로 XOR 문제 해결하기
|x1|x2|XOR|
|:--:|:--:|:--:|
|0|0|0(-)|
|0|1|1(+)|
|1|0|1(+)|
|1|1|0(-)|

다음과 같은 weight과 bias를 가진 network를 연결하면 원하는 XOR 결과가 나온다.  
![xor problem](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/xor_problem.png)  
1. <img src="https://latex.codecogs.com/svg.latex?\;$$\left[\begin{array}{rr}0&0\end{array}\right]$$$$\left[\begin{array}{r}5\\5\end{array}\right]$$-8=-8" title="xor example 1"/>, <img src="https://latex.codecogs.com/svg.latex?\;y_1=S(-8)=0" title="xor example 1"/>    
2. <img src="https://latex.codecogs.com/svg.latex?\;$$\left[\begin{array}{rr}0&0\end{array}\right]$$$$\left[\begin{array}{r}-7\\-7\end{array}\right]$$+3=3" title="xor example 1"/>, <img src="https://latex.codecogs.com/svg.latex?\;y_2=S(3)=1" title="xor example 2"/>    
3. <img src="https://latex.codecogs.com/svg.latex?\;$$\left[\begin{array}{rr}0&1\end{array}\right]$$$$\left[\begin{array}{r}-11\\-11\end{array}\right]$$+6=-11+6=-5" title="xor example 1"/>, <img src="https://latex.codecogs.com/svg.latex?\;\bar{y}=S(-5)=0" title="xor example 3"/>    

## 2. backpropagation
forward로 f를 계산하고 backward로 각 변수가 f에 미치는 영향을 계산한다. (미분 이용)  
