import tensorflow as tf

# tf Graph Input
X = [1,2,3]
Y = [1,2,3]

W = tf.Variable(tf.random_normal([1]), name='weight')

# Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_sum(tf.square(hypothesis - Y))

# Minimize: Gradient Descent Magic
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

for step in range(100):
    sess.run(train)
    print(step, sess.run(W))
