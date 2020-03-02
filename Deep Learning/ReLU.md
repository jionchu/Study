# ReLU (Rectified Linear Unit)

## 1. sigmoid function의 문제점
activation function으로 sigmoid 함수를 많이 사용했지만 **vanishing gradient**문제로 ReLU로 대체되었다.  

### Vanishing gradient
sigmoid function의 값은 0에서 1 사이이기 때문에 backpropagation을 수행하면 layer를 지나면서 값이 점점 작아져 최종 미분값은 0에 가까워진다. → layer가 많아지면 W 최소값을 제대로 찾지 못한다.  

## 2. ReLU function
![ReLU function](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/relu_function.png)  
vanishing gradient 문제를 해결하기 위해 activation function으로 ReLU를 사용한다. ReLU는 입력값이 0보다 작으면 0을, 0보다 크면 입력값을 그대로 출력한다.  

### ReLU의 장점
- Sparse activation: 0 이하의 입력에 대해 0을 출력함으로써 부분적으로 활성화 가능
- Efficient gradient propagation: gradient의 vanishing이 없고 gradient가 exploding 되지 않는다.
- Efficient computation: 선형함수이므로 미분 계산이 매우 간단
- Scale-invariant: <img src="https://latex.codecogs.com/svg.latex?\;max(0,ax)=amax(0,x)" title="scale invariant"/>

참고: https://mongxmongx2.tistory.com/25  