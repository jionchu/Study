# CNN
## 1. ConvNet
고양이 실험에서 시작된 아이디어  
고양이에게 그림을 보여주었을 때 뉴런들이 동시에 동작하는 것이 아니라 그림의 일부마다 반응하는 뉴런들이 다르다는 것을 알게 되었다.  
⇒ 여기에서 convolutional neural network를 만들게 됨  

Conv와 ReLU를 번갈아가면서 쌓다가 중간에 마지막에 FC(Fully Connected)를 실행한다.  

### Filter
- 이미지의 일부만 미리 처리한다 (=filter)
- filter의 사이즈는 정할 수 있음
- filter는 한 값을 만들어냄
- 이미지의 일부 영역을 filter를 통해서 하나의 점으로 만들어냄
- = Wx+b를 이용한다.
- ReLU를 이용하여 ReLU(Wx+b)를 할 수도 있다.

같은 필터를 이용해서 모든 영역에서 점을 뽑아낸다.
총 몇 개의 점(number)을 뽑아낼 수 있을까?  

![filter example](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/filter_example.png)  
Output size: (N-F)/stride + 1

#### example
N = 7, F = 3  
- stride 1 ⇒ (7-3)/1 +1 =5
- stride 2 ⇒ (7-3)/2 +1 =3
- stride 3 ⇒ (7-3)/3 +1 = 2.33

이미지가 계속 작아지는 문제점이 있음
⇒ padding: 테두리에 입력을 줌

### filter를 쓰는 이유
- 그림이 작아지는 것을 방지
- 이 부분이 모서리라는 것을 네트워크에 알려주기

#### example input 7x7
- 3x3 filter, applied with stride 1
- pad with 1 pixel border ⇒ what is the output?
- 7x7 output! ⇒ 같은 사이즈의 이미지가 나온다.

각각의 weight이 다른 filter들을 모두 convolution layer에 적용함  
⇒ 6개의 filter를 적용한 경우 activation maps의 shape은 (?,?,6)이 됨  
세 개 중 마지막은 항상 filter의 개수와 같고 앞의 두 개는 이미지 size와 filter size에 따라 결정됨    

![filter example](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/filter_example2.png)  
위의 경우 padding을 하지 않는다고 가정하면 (28,28,6)  

![filter example](https://github.com/jionchu/Study/blob/master/Deep%20Learning/images/filter_example3.png)  
convolution layer들의 weight 값은 어떻게 정하나?  
- 다른 neural network들과 같이 랜덤하게 초기화함  
- 우리가 가진 데이터로 학습해서 정해짐  

## 2. TensorFlow CNN basic
1. convolution layer로 값을 뽑아냄
2. sub sampling: 데이터를 작게 만듦
3. 나눠진 값들(feature extaction: 이미지에서 뽑아낸 특징)을 일반적인 forward neural net/fully connected layer를 통해 합침

Image: 1,3,3,1 image, Filter: 2,2,1(filter 색),1(filter 개수)  
Stride: 1x1, Padding:Valid  
tf.nn.conv2d 함수로 간단하게 구현 가능

### padding
SAME → filter의 size가 뭐든지 입력 영상과 출력 영상의 크기가 같게 나오게 해줌 → tensorflow가 알아서 필요한만큼 나머지 부분을 0으로 채움  
- filter의 개수만큼 출력 영상이 나옴 (하나의 입력에 여러개의 출력!)  
- convolution 후에는 pooling (subsampling) 하기  
실험해봤을 때 CNN과 잘 동작하기 때문에 대부분 Max Pooling을 쓴다.
```python
tf.nn.max_pool
```