from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding
import numpy as np

sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentenses)

sequences = tokenizer.texts_to_sequences(sentenses)

max_length = 4

X = pad_sequences(
    sequences,
    maxlen = max_length,
    padding = "pre"
)

vocab_size = len(tokenizer.word_index) + 1

Embedding_model = Sequential()
Embedding_model.add(Embedding(input_dim=vocab_size,output_dim=4))

Embedding_model.build(input_shape = (None,max_length))

Embedding_model.summary()

Embedding_output = Embedding_model.predict(X,verbose = 0)

print("Embedding Vector For first Sentence")
print("Sentence :",sentenses[0])
print("Padded Sequence :",X[0])

for position, token in enumerate(X[0]):
    print("Position :",position+1)
    print("Token :",token)
    print("Vector :",np.round(Embedding_output[0][position], 4))
