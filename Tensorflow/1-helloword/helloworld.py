#1 ioport 
#2 string
#3 print

import tensorflow as tf
hello = tf.constant('hello tf!')
sess = tf.Session()
print(sess.run(hello))
#常量sess print