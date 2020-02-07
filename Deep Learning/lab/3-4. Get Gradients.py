import tensorflow as tf

# tf Graph Input
X = [1,2,3]
Y = [1,2,3]

# Set wrong model weights
W = tf.Variable(5.0)

# Our hypothesis for linear model X * W
hypothesis = X * W

# Manual gradient
gradient = tf.reduce_mean((W * X - Y) * X) * 2
# cost/loss function
cost = tf.reduce_sum(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

# Get gradients
gvs = optimizer.copute_gradients(cost)
# Apply gradients
apply_gradients = optimizer.apply_gradients(gvs)

# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

for step in range(100):
    sess.run(apply_gradient)
    print(step, sess.run([gradient, W, gvs]))
