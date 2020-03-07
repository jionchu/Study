# RNN
### Sequence data
ex) 음성 인식  
- 하나의 단어만 이해한다고 되는게 아님
- 이전의 값이 다음 값에 영향을 줘야 함
- 기존의 NN/CNN은 이러한 sequence data를 처리하기 어려웠음

그래서 나온 모델이 RNN. 이전의 연산이 다음 연산에 영향을 미치기 때문에 series data에 적합하다.  
![RNN](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/rnn.png)  

## 1. RNN
### Recurrent Neural Network
각 RNN cell에서 y 값을 뽑아낸다.  
![RNN function](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/rnn_function.png)  
![RNN graph](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/rnn_graph.png)  
모든 RNN cell에 대한 연산 함수가 같기 때문에 하나의 그래프로 나타낼 수 있다.  

### (Vanilla) Recurrent Neural Network
기본적인 RNN  

<img src="https://latex.codecogs.com/svg.latex?\;h_t=f_W(h_{t-1},x_t)" title="rnn function"/>  
<img src="https://latex.codecogs.com/svg.latex?\;h_t=\tanh(W_{hh}h_{t-1}+W_{xh}x_t)" title="rnn function"/>  
<img src="https://latex.codecogs.com/svg.latex?\;y_t=W_{hy}h_t" title="rnn function"/>  
y가 몇 개의 vector로 나올 것인지는 W의 형태에 달려있다.  

### Character-level language model example
![Character level language model](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/rnn_character_level.png)  
이전의 글자를 보고 다음에 무슨 글자가 나올지 판단한다.  

### RNN application
- Language Modeling
- Speech Recognition
- Machine Translation
- Conversation Modeling/Question Answering
- Image/Video Captioning
- Image/Music/Dance Generation

### Multi-Layer RNN
더 복잡한 학습이 가능하다.  
![RNN Multi-Layer](https://github.com/jionchu/TIL/blob/master/Deep%20Learning/images/rnn_multi_layer.png)  

### Training RNNs is challenging
Vanilla RNN도 layer들이 많아지면 학습에 어려움이 있음  

### Several advanced models
- Long Short Term Memory (LSTM)
- GRU by Cho et al, 2014
