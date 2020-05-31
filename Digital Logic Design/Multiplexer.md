# Multiplexer

A multiplexer (MUX) circuit has
- A number of data inputs
- One (or more) select inputs
- **One output**

- 여러 개의 입력 신호 중 특정 조건(select signal)에 따라 입력 신호를 한 개만 선택

## 1. Multiplexer implementations
### 1) 2-input multiplexer
- select signal 1개

![2-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/2-input_mux.PNG)  

### 2) 4-input multiplexer
- select signal 2개

![4-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/4-input_mux.PNG)  
![4-input mux truth table](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/2-input_mux_truth_table.PNG)  

### 3) 4-input multiplexer using 2-input multiplexer
![4-input mux using 2-input mux](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/4-input_mux_using_2-input_mux.PNG)  

## 2. MUX application
### 1) 2x2 crossbar
- 신호가 교차해서 넘어가는 것
- s 값에 따라 2가지 상태 중 하나를 선택할 수 있음
- x1:y1 & x2:y2
- x1:y2 & x2:y1

![crossbar](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/crossbar.PNG)  

### 2) switch
- programmable device에서 사용됨

![switch](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/switch.PNG)  

## 3. Logic functions using MUXs
- 입력 데이터를 select signal로 사용하여 회로를 간소화 할 수 있음
- ex) 입력이 a=0, b=0 & a=0, b=1인 경우를 묶어서 하나의 출력(ex. 1 or 0 or b' ...)으로 나타냄

### 1) XOR
![xor](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/mux_xor.PNG)  

- 위의 회로는 아래의 회로와 같이 간소화 할 수 있음

![simple xor](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/mux_xor_simplify.PNG)  

### 2) 3-input XOR
![3-input xor](https://github.com/jionchu/TIL/blob/master/Digital%20Login%20Design/images/mux_3-input_xor.PNG)  
