# Max pooling, FC layer

## 1. Max pooling
### polling layer
sampling이라고도 한다.  
convolution layer에서 하나만 뽑아내서 resize하는 것  
한 layer씩 뽑아서 sampling하고 다시 모아서 다음 단계로 넘긴다.  
![sampling](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/sampling.png)  

### Max polling
sampling 할 때 가장 큰 값을 넘기는 것  
![max pooling](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/max_pooling.png)  

## 2. Fully Connected Layer (FC layer)
이전 레이어의 모든 노드가 다음 레이어의 모든 노드에 연결된 layer  
layer들을 원하는 대로 쌓은 다음에 마지막에 pooling을 한다.  
이 결과를 fc(=앞에서 배운 softmax 등등)에 넣고 나온 게 최종 결과가 된다.  
![cnn layers](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/cnn.png)  