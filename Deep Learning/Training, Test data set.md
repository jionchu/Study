# Training, Test data set

### performance evaluation
모델이 잘 작동하는지 확인하기  
Training set을 이용하면 될까? ⇒ X. 모델(알고리즘)이 training data를 기억하고 있기 때문에 정확도가 100%가 나오게 된다.  

### test data set
data set의 일부는 test data set으로 남겨두고 학습에 이용하지 않는다.  
training set을 가지고 모델을 학습시킨 다음 test set으로 정확도를 검증한다.  

![data set groups](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/data_set_group.png)  
- training set으로 학습을 시키고 validation set을 이용하여 <img src="https://latex.codecogs.com/svg.latex?\;\alpha" title="alpha" />, <img src="https://latex.codecogs.com/svg.latex?\;\lambda" title="lambda" />의 값을 튜닝한다. (=모의고사)  
- validation set으로 튜닝이 완전하게 되면 test set을 이용하여 실제로 모델이 잘 동작하는지 확인한다. (test data set은 단 한번만 볼 수 있다.)  

일반적으로 training set/testing set 두 개로 나누고 validation set까지 3개로 나눌 때도 있다.  

### online learning
data set이 너무 많은 경우 한번에 다 넣어서 학습시키기 힘들기 때문에 **online learning**이라는 학습방법을 사용한다.  
data set을 여러 개로 나누어서 앞의 data들을 먼저 학습시키고 그 결과를 model에 저장해두고 다음 data들을 추가로 학습시킨다. → 굉장히 좋은 모델  
새로운 데이터가 추가된 경우 이전의 데이터들을 새로 학습시키지 않고 기존에 있는 데이터에 추가로 학습시킬 수 있다.  
