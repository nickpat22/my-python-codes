import tensorflow as tf

tensor1 = tf.constant([10,20,30])
tensor2 = tf.constant([1,2,3])

addition = tf.add(tensor1,tensor2)
print("Addition is : ",addition) #[11,22,33]

substraction = tf.subtract(tensor1,tensor2)
print("Substraction is : ",substraction)    #[9,18,27]

Multiplication = tf.multiply(tensor1,tensor2)
print("Multiplication is : ",Multiplication) #[10,40,90]

Division = tf.divide(tensor1,tensor2)
print("Division is : ",Division) #10.0 , 10.0, 10.0

Square = tf.square(tensor1) #100, 400, 900
print("Square is : ",Square)

sum = tf.reduce_sum(tensor1) #60
print("Reduced Sum is : ",sum)

mean = tf.reduce_mean(tensor1) #20
print("Mean is :",mean)