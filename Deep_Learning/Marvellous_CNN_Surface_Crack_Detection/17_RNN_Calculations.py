# ht = tanh[Wx*Xt + Wh* ht-1 + b)'

import numpy as np

def segmoid(x):
    return 1/(1+np.exp(-x))

def MarvellousRNNPrediction():
    print("Calculations of RNN")
    # Food was not good
    inputs = [1,2,5,3] 

    hidden_state = 0 #Rnn Parameters
    Wx = 0.5
    Wh = 0.8
    bias = 0.1

    # RNN Calculations
    for time_step, x in enumerate(inputs):
        previous_hidden_State = hidden_state

        weighte_inpur = Wx * x
        weighte_memory = Wh * previous_hidden_State

        total = weighte_inpur + weighte_memory + bias

        hidden_state = np.tanh(total)

        print("Time Step : ",time_step)
        print("input :",x)
        print("Hidden State :",hidden_state)
        print("-"*30)

    # Stwp 2 : final Hidden State
    print("Final Hidden State : ",hidden_state)


    # Step 3 : Output Layer
    # output = Wy * finalhiddenstate + output_Bias
     
    Wy = 1.0
    output_bias = 0.0

    output = (Wy * hidden_state) + output_bias

    print("Raw output : ",output)

    # Step 4 : Apply the Sigmoid 

    probablity = segmoid(output)

    print("Probablity is : ",probablity)

    #Step 5 : Final Calculations

    if probablity <= 0.5:
        print("Positive")
    else:
        ("Negative")



def main():
    MarvellousRNNPrediction()

if __name__ == "__main__":
    main()