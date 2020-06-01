# Multiplexer

A multiplexer (MUX) circuit has
- A number of data inputs
- One (or more) select inputs
- **One output**

- 여러 개의 입력 신호 중 특정 조건(select signal)에 따라 입력 신호를 한 개만 선택

## 1. Multiplexer implementations
### 1) 2-input multiplexer
- select signal 1개

![2-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/2-input_mux.PNG)  

### 2) 4-input multiplexer
- select signal 2개

![4-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/4-input_mux.PNG)  
![4-input mux truth table](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/4-input_mux_truth_table.PNG)  

### 3) 4-input multiplexer using 2-input multiplexer
![4-input mux using 2-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/4-input_mux_using_2-input_mux.PNG)  

## 2. MUX application
### 1) 2x2 crossbar
- 신호가 교차해서 넘어가는 것
- s 값에 따라 2가지 상태 중 하나를 선택할 수 있음
- x1:y1 & x2:y2
- x1:y2 & x2:y1

![crossbar](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/crossbar.PNG)  

### 2) switch
- programmable device에서 사용됨

![switch](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/switch.PNG)  

## 3. Logic functions using MUXs
- 입력 데이터를 select signal로 사용하여 회로를 간소화 할 수 있음
- ex) 입력이 a=0, b=0 & a=0, b=1인 경우를 묶어서 하나의 출력(ex. 1 or 0 or b' ...)으로 나타냄

### 1) XOR
![xor](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/mux_xor.PNG)  

- 위의 회로는 아래의 회로와 같이 간소화 할 수 있음

![simple xor](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/mux_xor_simplify.PNG)  

### 2) 3-input XOR
![3-input xor](https://github.com/jionchu/TIL/blob/master/Digital%20Logic%20Design/images/mux_3-input_xor.PNG)  

## 4. Shannon's expansion theorem
여러 개의 input이 있을 때, input 중 하나의 값으로 묶어서 식을 정리할 수 있음  

### 1) example 1
|x|y|z|f|
|---|---|---|---|
|0|0|0|0|
|0|0|1|0|
|0|1|0|0|
|0|1|1|1|
|1|0|0|0|
|1|0|1|1|
|1|1|0|1|
|1|1|1|1|

|x|f|
|---|:---:|
|0|yz|
|1|y+z|

f = x'(yz) + x(y + z)

### 2) example 2
|x|y|z|f|
|---|---|---|---|
|0|0|0|0|
|0|0|1|1|
|0|1|0|0|
|0|1|1|1|
|1|0|0|0|
|1|0|1|1|
|1|1|0|1|
|1|1|1|1|

|x|f|
|---|:---:|
|0|z|
|1|y+z|

f = x'(z) + x(y + z)

### 3) example 3
|x|y|z|f|
|---|---|---|---|
|0|0|0|1|
|0|0|1|1|
|0|1|0|0|
|0|1|1|1|
|1|0|0|1|
|1|0|1|1|
|1|1|0|0|
|1|1|1|0|

f = x'y'z' + x'y'z + x'yz + xy'z' + xy'z  

#### ㄱ. choose x as the expansion variable
⇒ f = x'(y'z' + y'z + yz) + x(y'z' + y'z)  
⇒ f = x'(y' + z) + x(y')  

#### ㄴ. choose z as the expansion variable
⇒ f = z'(x'y' + xy) + z(x'y' + x'y + xy')  
⇒ f = z'(y') + z'((xy)')  
