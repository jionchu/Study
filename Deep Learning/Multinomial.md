# Multinomial
여러 개의 클래스가 있을 때 그것을 예측하는 것  
softmax classification: multinomial classification 중에서 가장 많이 쓰이는 것

logistic regression을 학습시킨다는 것은 두 집단을 구분하는 선을 찾는 것이다. 만약 세 집단이 있다면 구분하는 선을 어떻게 찾을 것인가?  

세 개의 각각 다른 binary classification을 이용해서 구현 가능  

하지만 세 개를 독립적으로 구현하는 것은 복잡하므로 하나로 합친다.  

이렇게 하면 하나의 classification이 독립된 classification처럼 동작하게 된다.  
