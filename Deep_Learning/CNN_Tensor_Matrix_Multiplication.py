import tensorflow as tf

matrix1 = tf.constant([
    [1,2],
    [3,4]
],dtype=tf.float32)

matrix2 = tf.constant([
    [5,6],
    [7,8]
],dtype=tf.float32)

result = tf.matmul(matrix1,matrix2)

print(result)