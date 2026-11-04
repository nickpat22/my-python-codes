import numpy as np

def ReLU(z):
    return max(0,z)

def Marvellous_Neuron_Forward(inputs,Weights,bias):
    print("Inputs are (x): ",inputs)
    print("Weights are (w):",Weights)
    print("bias (b) :",bias)

    #z = sum(w * x for w, x in zip(Weights,inputs)) + bias
    z = 0
    for i in range(len(inputs)):
        z = z + (inputs[i] * Weights[i])

    z = z + bias

    
    print("Weightd Sum (z) : ",z)

    y = ReLU(z)

    return y

def main():
    print("---------Marvellous Nural Network-----")

    inputs = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    result = Marvellous_Neuron_Forward(inputs,weights,bias)

    print("Predicted Result :",result)

if __name__ == "__main__":
    main()