import tensorflow as tf
import numpy as np

def hello_world():
	hello = tf.constant('Hello, TensorFlow World!')
	sess = tf.Session()
	print(sess.run(hello))

#—————————————————————————————

def math_operation_graph():
	#Module 2

	#a * b + c/d

	a = tf.constant(6, name='constant_a') #a,b,c,d are tensors (data)
	b = tf.constant(3, name='constant_b')#Name so we can visualise on tensorboard
	c = tf.constant(10, name='constant_c')
	d = tf.constant(5, name='constant_d')

	mul = tf.multiply(a, b, name="mul") #mul,div are nodes
	div = tf.div(c, d, name="div")

	addn = tf.add_n([mul, div], name="addn")

	print (addn) #Will print the object, not created the graph yet so dont know the value.
	print (a)
	print (mul)

	sess = tf.Session() #Session supervises the execution of TensorFlow graphs
	sess.run(addn) #Will run the full graph as addn is the last operation

	sess.run(mul) #Will only run first node.

	sess.run(div) #First node also.

	writer = tf.summary.FileWriter('./m1_example1', sess.graph) #Writes to output so can visualise in tfboard
	writer.close() #Standard close writer.

	sess.close() #Close tf sess


	#tensorboard --logdir="m1_example1"

#—————————————————————————————

def ranks():

	sess = tf.Session()

	zeroD = tf.constant(5)
	sess.run(tf.rank(zeroD))

	oneD = tf.constant(["How", "are", "you?"])
	sess.run(tf.rank(oneD))

	twoD = tf.constant([[1.0, 2.3], [1.5, 2.9]])
	sess.run(tf.rank(twoD))

	threeD = tf.constant([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
	sess.run(tf.rank(threeD))

	sess.close()


#—————————————————————————————


def numpy_example():
	sess = tf.Session()

	zeroD = np.array(30, dtype=np.int32)
	sess.run(tf.rank(zeroD)) #Rank is the number of dimensions in a tensor
	sess.run(tf.shape(zeroD)) #Shape is the number of elements in each dimensions


	oneD = np.array([5.6, 6.3, 8.9, 9.0], dtype=np.float32)
	sess.run(tf.rank(oneD))
	sess.run(tf.shape(oneD))

	sess.close()

#—————————————————————————————

def interactive_session():

	with tf.Session() as sess:

		sess = tf.InteractiveSession()

		A = tf.constant([4], tf.int32, name='A')
		x = tf.placeholder(tf.int32, name='x')

		y = A * x

		y.eval(feed_dict={x: [5]})

	sess.close()

#—————————————————————————————

def main():
	hello_world()
	math_operation_graph()
	ranks()
	numpy_example()
	interactive_session()


if __name__ == "__main__" : main()














