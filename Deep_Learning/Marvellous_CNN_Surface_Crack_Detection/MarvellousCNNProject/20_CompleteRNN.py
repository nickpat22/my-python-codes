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
max_length = 4
#Step 2 : Tokeniaztion

tokenizer = Tokenizer(oov_token = "<oov>")

tokenizer.fit_on_texts(train_Sentenses)

#Step 3 : Conver Training Data into Sequence 

train_sequence = tokenizer.texts_to_sequences(train_Sentenses)

print("Training Sequences :")

for sentence, sequece in zip(train_Sentenses,train_sequence):
    print(sentence,"->",sequece)

#Step 4 : Apply Padding

X_train = pad_sequences(
    train_sequence,
    maxlen = max_length,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded Training Data")
print(X_train)

print("Training labes :")
print(Y_train)

# Step 5 :  Calculate Vocablary Size

vocab_size = len(tokenizer.word_index) + 1

print("Vocab",vocab_size)

#Step 6 ; build Model

model = Sequential()

model.add(
    Embedding(
        input_dim = vocab_size,
        output_dim=8,
        input_length=max_length
    )
)


model.add(
    SimpleRNN(
        units =8,
        activation = "tanh"
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)

# step 7 : Compile the model
model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

#Step : 8 Display

model.build(input_shape = (None, max_length))

print("Model Architecture")
model.summary()

#Step 9 : tar   

history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)

print("Model Training Completed")


# 10 Crete unseen Data

test_sentences = [
    "Service was amazing",
    "Service was horribel",
    "Experience was Horrible",
    "Experience was Terrible"
]

# Step 11 : Conver text to Sequence

test_sequences = tokenizer.texts_to_sequences(test_sentences)

X_test = pad_sequences(
    test_sequences,
    maxlen = max_length,
    padding = "pre"
    )

# Predict the Sentiment 

for text,sequence,padded in zip(test_sentences,test_sequences,X_test):
    input_data = np.array([padded])

    pridiction = model.predict(input_data,verbose = 0)

    probablity = float(pridiction[0][0])

    print("Sentance : ",text)
    print("Sequance : ",sequence)
    print("Padded sequance : ",padded)
    print("Prediction : ",probablity)

    if probablity >= 0.5:
        print("Sentiment : Positive")
    else:
        print("Sentiment : Negative")