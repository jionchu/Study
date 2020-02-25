# Deep learning basic concepts

### activation function
생각하는 기계를 만들자!  
뇌가 굉장히 복잡하게 연결되어 있고 뉴런이라는 유닛이 굉장히 단순하게 동작한다는 것에 사람들은 놀람  
- input x*W(weight) + bias로 계산되어 전달됨  
- 어떤 값 이상이면 활성화 되고 아니면 활성화 되지 않음
이러한 뉴런은 수학적으로 만들 수 있겠다 해서 activation function을 만듦  

## 1. XOR problem
OR과 AND의 경우 linear하게 구분이 되었지만 XOR의 경우 명확하게 linear하게 구분되지 않는 문제점이 발생함 -> 한 개로는 불가능하고 MLP(multilayer perceptrons)를 사용하면 가능. 하지만 각각에 들어갈 weight과 bias를 학습시킬 수 없다.  

### Backpropagation
위의 문제가 나중에 해결됨 (Backpropagation)  
→ 출력을 만들어내고 맞는지 확인하고 다시 weight과 bias를 재설정
더 복잡한 형태의 예측이 가능해짐

### Convolutional Neural Networks
CNN도 weight과 bias를 학습시키는 또다른 방법이다.  

고양이 실험을 해보니 사진마다 활성화되는 뉴런이 다름 → 신경망 세포가 동시에 전체를 보는 것이 아니라 일부를 담당하는 신경망이 있고 나중에 조합되는 것이 아닌가 하는 생각에서 나옴  

- 90% 이상의 성능을 보여줌 (특히 이미지나 문자를 읽는 부분)

하지만, Backpropagation이 복잡한 문제를 풀기 위해서는 최소 10여개의 layer를 학습시켜야 함. 결과에서 발견되었던 error가 layer를 거치면서 점점 약해져서 학습이 제대로 이루어지지 않음 → 많이 할수록 오히려 성능이 떨어짐
→ 다른 알고리즘들이 떠오르게 됨 (SVM, RandomForest...)

시간이 지나고 layer가 deep해지면 학습할 수 없다는 것이 틀리고 초기값만 잘 주면 학습할 수 있음을 보여줌  
Neural Network라고 하면 사람들이 이미 실패한 것이라고 관심갖지 않아서 **Deep Learning**이라고 이름을 바꿈