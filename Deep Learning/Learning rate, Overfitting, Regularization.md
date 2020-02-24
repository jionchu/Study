# Learning rate, Overffiting, Regularization

## 1. Learning rate
learning rate를 잘 정하는 것이 중요하다.  
- learning rate가 너무 크면 학습이 이루어지지 않는다. → overshooting
- learning rate가 너무 작으면 학습이 너무 오래 걸린다. → local minimum에서 멈출 수 있다.  
![learning rate problems](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/overshooting,%20local%20minimum.png)  

### Try several learning rates
- cost function 값을 확인해보기
- resonable rate로 내려가고 있는지 확인하기

## 2. Data preprocessing for gradient descent
x 데이터를 전처리해야 하는 경우가 있다.  
x1과 x2의 차이가 커서 등고선이 왜곡되어 있을 때, normalize를 해 줄 필요가 있다.  
- 중심이 0으로 가도록 조절
- 전체 값이 어떤 값 영역 안에 들어가도록 조절

### standardization
normalization 중 하나

## 3. Overfitting
학습 데이터에 너무 잘 맞는 모델을 만든 경우, 실제 데이터에는 잘 맞지 않는 경우가 발생한다. 일반적인 모델을 만들어야 다른 데이터가 들어와도 잘 맞는다.  

### Overfitting을 해결하는 방법
- 많은 양의 training data
- feature의 개수 줄이기
- Regularization (일반화)

### Regularization
weight이 큰 값을 가질수록 그래프가 구부러지게 된다. 구부러진 부분들을 펴기 위해서 weight의 값을 줄인다.  
