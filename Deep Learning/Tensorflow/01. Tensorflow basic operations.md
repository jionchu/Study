# 01. Tensorflow basic operations

## 1. About Tensorflow
### Tensorflow
Tensorflow는 data flow graph를 이용한 수학 연산을 하기 위한 오픈 소스 라이브러리로, 많은 딥러닝 라이브러리들 중 사용자가 가장 많은 라이브러리이다.

### Data Flow Graph
- Graph의 node는 수학적 operation을 의미한다.
- Graph의 edge는 node들 사이의 data array(tensor)를 의미한다.

## 2. Tensorflow start
### Tensorflow version check
tensorflow 설치 후 설치된 버전을 확인해보자.
```python
import tensorflow as tf
tf.__version__
```

### TensorFlow Hello World!
```python
# Create a constant op
# This op is added as a node to the default graph
hello = tf.constant("Hello, TensorFlow!")

# set a tf session
sess = tf.Session()

# run the session and get result
print(sess.run(hello))
```

### Conputational Graph
```python
node1 = tf.constant(3.0.tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
node3 = tf.add(node1, node2) # node3 = node1 + node2

print("node1:", node1, "node2:", node2)
print("node13:", node3)

sess = tf.Session()
print("sess.run(node1, node2):", sess.run([node1, node2]))
print("sess.run(node3):", sess.run(node3))
```

### TensorFlow Mechanics
1. Graph Build
2. sess.run
3. Updata variables & return values

### Placeholder
값을 지정해두지 않고 비어있는 채로 생성하여 사용자의 입력을 기다리는 노드
```python
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + provides a shortcut for tf.add(a,b)

sess = tf.Session()
print(sess.run(adder_node, feed_dict={a:3, b:4.5}))
print(sess.run(adder_node, feed_dict={a:[1,3], b:[2,4]}))
```

### Tensor Ranks, Shapes, and Types
대부분 float32를 사용한다.
