# Decoder, Demultiplexers, Encoders and Code Converters

## 1. Decoder
- decode encoded information
- binary decoder has **n** data inputs and **2^n** outputs
- 여러 개의 output 중 하나만 1로 출력됨 (**one-hot encoded**)
- Enable input(En)이 사용됨
  - En = 0 : 모든 output이 0 (작동하지 않음)
  - En = 1 : input에 따라 다른 output이 출력됨

### 1) 2-to-4 decoder
|En|w1|w2|y0|y1|y2|y3|
|---|---|---|---|---|---|---|
|1|0|0|1|0|0|0|
|1|0|1|0|1|0|0|
|1|1|0|0|0|1|0|
|1|1|1|0|0|0|1|
|0|X|X|0|0|0|0|

![2-to-4 decoder](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/2-to-4_decoder.PNG)  

### 2) 3-to-8 decoder
![3-to-8 decoder](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/3-to-8_decoder.PNG)  

### 3) 74138 3-to-8 decoder
![74138 3-to-8 decoder](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/74138_3-to-8_decoder.PNG)  

## 2. Demultiplexer
- distributor (분배기)
- 여러 개의 input 중 하나를 선택해서 출력하는 multiplexer와 반대
- n-to-2^n decoder가 1-to-n demultiplexer로 구현됨

