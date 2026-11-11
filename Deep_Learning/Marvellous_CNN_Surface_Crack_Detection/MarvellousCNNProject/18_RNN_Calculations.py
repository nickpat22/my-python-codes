import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

#Step 1 Load the Data
train_Sentenses = [
    "Food was Good",
    "Food was bad",
    "Food was Excellent",
    "Food was Teribal",
    "Service was Good",
    "Srvice was bad",
    "service was excellent",
    "Service was Teribel",
    "Ambience was Good",
    "Ambience was bad",
    "Ambience was excellent",
    "Ambience was Teribel"
]

train_labels =[
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

#Step 2 : Tokeniaztion

tokenizer = Tokenizer(oov_token = "<oov>")

tokenizer.fit_on_texts(train_Sentenses)

#Step 3 : Conver Training Data into Sequence 

train_sequence = tokenizer.texts_to_sequences(train_Sentenses)

print("Training Sequences :")

for sentence, sequece in zip(train_Sentenses,train_sequence):
    print(sentence,"->",sequece)