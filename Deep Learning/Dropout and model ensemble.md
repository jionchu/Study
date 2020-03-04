# Dropout and model ensemble

## 1. Overffiting
overfitting 됐는지 어떻게 확인할까?
- Very high accuracy on the training data set (ex: 0.99)
- Poor accuracy on the test data set (0.85)

layer가 많을수록 train data set에서 error는 떨어지지만 test data set에서는 overfitting되어서 error가 다시 올라가게 된다.  

### Solution for overffiting
- More training data set
- Regularization

## 2. Regularization
모델을 쉽게 만드는 방법은 단순하게 cost function의 값이 작아지는 방향으로 진행하는 것인데 이 경우 특정 weight이 너무 큰 값을 가져 overffiting이 발생할 수 있다.  

Regularization은 특정 weight이 너무 커지지 않게 조절한다.  

### Regularization의 종류
- L1 Regularization
- L2 Regularization
- Dropout
- Early stopping

## 3. Dropout
일종의 regularization의 방법  
random하게 어떤 노드들을 끄고 (0으로 만들고) 계산한다.  
train할 때만 dropout 되기 때문에 모델을 평가할 때는 dropout_rate를 1로 줘야 함 (dropout하는게 없다는 의미)  
![dropout](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/dropout.PNG)  

### Dropout의 장점
- 다양한 모델을 학습시켜서 결합하는 것과 같은 효과를 얻는다.  
- 학습을 시키다 보면 학습 데이터에 의해 weight들이 서로 동조화되는 현상이 발생할 수 있는데 무작위로 생략을 하면서 이러한 현상을 피할 수 있다.

## 4. Ensemble
데이터를 여러 개의 training set으로 나누어 동시에 학습을 진행한 다음 모든 학습이 끝나면 독립된 여러 개의 모델을 합치는 것  
![model ensemble](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/model_ensemble.png)  
머신 러닝 기술을 이용하여 실세계의 문제를 해결하고자 한다면 앙상블 방법은 필수이다.  

참고: https://light-tree.tistory.com/125  
https://m.blog.naver.com/PostView.nhn?blogId=laonple&logNo=220818841217&proxyReferer=https%3A%2F%2Fwww.google.com%2F  
https://untitledtblog.tistory.com/156  