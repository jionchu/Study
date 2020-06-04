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

## 3. Encoder
- decoder와 반대되는 기능
- binary encoder has **2^n** data inputs and **n** outputs
- 여러 개의 input 중 하나만 1로 들어옴
- information을 표현하는 데 필요한 bit 수를 줄여줌

### 1) 2^n-to-n binary encoder
|w3|w2|w1|w0|y1|y0|
|---|---|---|---|---|---|
|0|0|0|1|0|0|
|0|0|1|0|0|1|
|0|1|0|0|1|0|
|1|0|0|0|1|1|

### 2) Priority encoders
- 가장 높은 자리 bit 값만 인정하고 나머지는 무시함
- 우선순위 encoder

|w3|w2|w1|w0|y1|y0|z|
|---|---|---|---|---|---|---|
|0|0|0|0|D|D|0|
|0|0|0|1|0|0|1|
|0|0|1|X|0|1|1|
|0|1|X|X|1|0|1|
|1|X|X|X|1|1|1|

- y0 = w0 + w1, y1 = w2 + w3
- z = w0 + w1 + w2 + w3

## 4. Code Converter
- convert from one type of nput encoding to another type of output encoding
- ex) 3-to-8 decoder converts binary number → one-hot encoding

### 1) BCD-to-7-segment decoder
- convert a BCD digit into 7 signals

|w3|w2|w1|w0|a|b|c|d|e|f|g|
|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|1|1|1|1|1|1|0|
|0|0|0|1|1|0|1|1|0|0|0|
|0|0|1|0|1|1|0|1|1|0|1|
|0|0|1|1|1|1|1|1|0|0|1|
|0|1|0|0|0|1|1|0|0|1|1|
|0|1|0|1|1|0|1|1|0|1|1|
|0|1|1|0|1|0|1|1|1|1|1|
|0|1|1|1|1|1|1|0|0|0|0|
|1|0|0|0|1|1|1|1|1|1|1|
|1|0|0|1|1|1|1|1|0|1|1|

![bcd-to-7-segment decoder](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/bcd-to-7-segment_decoder.PNG)  