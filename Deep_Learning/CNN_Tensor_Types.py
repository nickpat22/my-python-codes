import tensorflow as tf

#Scaller Tensor #0D Tensor

scaller_tensor = tf.constant(11)

print("Scaller Tensor : ",scaller_tensor)

#1D Tensor (Vector)

vector_tensor = tf.constant([11,21,51,101])

print("Vecor Tensot :",vector_tensor)

# 2D tensor (Matrics)

matrics_tensor = tf.constant([[10,20,30],[40,50,60]])

print("Matric Tensor : ",matrics_tensor)

# 3D tensor

tensor_3d = tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[7,8],[9,10]]
])

print("3D tensor : ",tensor_3d)
