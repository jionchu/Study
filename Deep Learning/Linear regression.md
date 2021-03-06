# 02. Linear Regression

## 1. Hypothesis & Cost of Linear Regression
### (Linear) Hypothesis  
- <img src="https://latex.codecogs.com/svg.latex?\;H(x)=W(x)+b" title="hypothesis" />
- 실제 데이터에 맞는 선을 찾는 것

### Cost (Lost) function
- <img src="https://latex.codecogs.com/svg.latex?\;cost(W,b)=\frac{1}{m}\sum_{i=1}^{m}(H(x^{(i)})-y^{(i)})^2" title="cost_function" />
- 가설과 실제 데이터의 차이
- cost 값이 작을수록 좋은 가설
- cost 값이 가장 작은 W와 b를 찾는 과정을 __학습__ 이라고 한다.

## 2. Tensorflow로 간단한 linear regression 구현하기
- Hypothesis란? 주어진 x 값에 대하여 어떻게 예측할 것인가
- cost 함수는 W와 b의 변화에 따라 값이 달라질 수 있음
- 학습이란? W와 b의 값을 조절하여 cost 값을 minimize하는 것

## 1) Build graph using TF operations
### X and Y data
- x=1일 때 y=1, x=2일 때 y=2, x=3일 때 y=3인 경우

```python
x_train = [1,2,3]
y_train = [1,2,3]
```
### Variable
- tensorflow가 자체적으로 변경시키는 값
- trainable variable이라고 볼 수도 있음
- tensorflow가 스스로 학습시키는 과정에서 변경시킴
- random_normal 안의 숫자는 shape을 나타냄

```python
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
```
### Hypothesis
<img src="https://latex.codecogs.com/svg.latex?\;H(x)=W(x)+b" title="hypothesis"/>

```python
hypothesis = x_train * W + b
```
### Cost/loss funtion
- <img src="https://latex.codecogs.com/svg.latex?\;cost(W,b)=\frac{1}{m}\sum_{i=1}^{m}(H(x^{(i)})-y^{(i)})^2" title="cost_function" />
- reduce_mean: tensor(값)들이 주어졌을 때 평균을 내 주는 함수
```python
cost = tf.reduce_mean(tf.square(hypothesis - y_train))
```
### Minimize
- tensorflow에는 여러 가지 방법이 있지만 그 중에 한 가지 __Gradient Descent__ 를 이용
- 무엇을 minimize할 것인지 optimizer의 minimize함수에 전달
- → tensorflow가 W와 b 값을 조절하여 알아서 minimize함 ⇒ Magic!!
```python
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
```

## 2) Run/update graph and get results
- Launch the graph in a session
- Initializes global variables in the graph
- tensorflow의 variable(ex: W, b)을 사용하여 실행하기 전에 꼭 초기화해줘야 함
- 값을 실행시킨다(run)는 말은 값을 가져온다는 의미

```python
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
```

## 3) placeholder 이용
### placeholder
- 미리 만들어놓은 그래프에 값만 바꿔서 넣을 수 있음

### X and Y data
```python
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
```
### Hypothesis
```python
# Our hypothesis XW+b
hypothesis = X * W + b
```
### Cost/loss function
```python
cost = tf.reduce_mean(tf.square(hypothesis - Y))
```
### Run/update graph and get results
- feed_dict로 placeholder에 값 넣기
```python
# Fit the line
for step in range(2001):
    cost_val, W_val, b_val, _ = \
        sess.run([cost, W, b, train], feed_dict={X:[1,2,3], Y:[1,2,3]})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)
```