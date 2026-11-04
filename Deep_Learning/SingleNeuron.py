import numpy as np


#Step 1 : Define input features i.e X
#                   [x1,x2,x3]
input = np.array([2.0,3.0,4.0])

print(" x : ",input)
#Step 2 : Define weights i.e w
#                    [w1,w2,w3]

weights = np.array([0.5,0.3,0.2])
print(" w : ",weights)


#Step 3 : Define Bias i.e b
#        b
bias = 1.0
print(" b : ",bias)


# step 4 : Calculate weighted Sum i.e Z
# Z = x1 w1 + X2 w2 + x3 w3 + b
# Z = (2.0*0.5 + 3.0 * 0.3 + 4.0 * 0.2) + 1.0

Z = np.dot(input,weights) + bias

print("Z : ",Z)

#Step 5  : Activation Function (ReLU)

def ReLU(x):
    return max(0,x)

#Step 6 : Final OP

Y =ReLU(Z)

print("Y : ",Y)




