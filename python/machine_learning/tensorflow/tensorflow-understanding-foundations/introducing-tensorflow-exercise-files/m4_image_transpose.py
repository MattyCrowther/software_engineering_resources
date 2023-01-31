import tensorflow as tf
import matplotlib.image as mp_img
import matplotlib.pyplot as plot
import os

filename = "./883518.JPG"

image = mp_img.imread(filename)

print ("Image shape: ", image.shape)
print ("Image array: ", image)

plot.imshow(image)
plot.show()

x = tf.Variable(image, name='x')

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)

	transpose = tf.image.transpose_image(x) #Flips image x,y values

	result = sess.run(transpose)

	print ("Transposed image shape: ", result.shape)
	plot.imshow(result)
	plot.show()
