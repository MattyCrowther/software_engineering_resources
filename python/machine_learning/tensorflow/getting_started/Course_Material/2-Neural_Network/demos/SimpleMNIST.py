#
#   SimpleMNIST.py 
#   Simple NN to classify handwritten digits from MNIST dataset
#

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data #MNIST data from tensorflow

# We use the TF helper function to pull down the data from the MNIST site
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) #one_hot gives us digit asociated with image (0-9) also returns only highest probablity of which digit it represents

# x is placeholder for the 28 X 28 image data
x = tf.placeholder(tf.float32, shape=[None, 784], name="images") #None is because we don't know how many images are passed in,  784 (28p*28p) creates list with 784 elements

# y_ is called "y bar" and is a 10 element vector, containing the predicted probability of each 
#   digit(0-9) class.  Such as [0.14, 0.8, 0,0,0,0,0,0,0, 0.06]
y_ = tf.placeholder(tf.float32, [None, 10])  

# define weights and balances. Creates a tensor with all elements set to zero.
W = tf.Variable(tf.zeros([784, 10])) #783 pixels, image could be numbers 0-9 and create list of all 0's because it will be changed later.
b = tf.Variable(tf.zeros([10])) #Only one bias per neuron

# define our inference model
#softmax is equivalent = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)
y = tf.nn.softmax(tf.matmul(x, W) + b) #Matmul is matrix multiplication

# loss is cross entropy
cross_entropy = tf.reduce_mean(
                tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))#softmax_cross_entropy_with_logits is difference between prediction and actual value.

# each training step in gradient decent we want to minimize cross entropy
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# initialize the global variables
init = tf.global_variables_initializer()

# create an interactive session that can span multiple code blocks.  Don't 
# forget to explicity close the session with sess.close()
sess = tf.Session()

# perform the initialization which is only the initialization of all global variables
sess.run(init)

# Perform 1000 training steps
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)    # get 100 random data points from the data. batch_xs = image, 
                                                        # batch_ys = digit(0-9) class
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}) # do the optimization with this data

# Evaluate how well the model did. Do this by comparing the digit with the highest probability in 
#    actual (y) and predicted (y_).
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1)) #Return points to a tensor that is True,False,False etc based on results. y is our predictoon y_ is actual value.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) #Converts to binary predicate 0,1
test_accuracy = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print("Test Accuracy: {0}%".format(test_accuracy * 100.0))

sess.close()