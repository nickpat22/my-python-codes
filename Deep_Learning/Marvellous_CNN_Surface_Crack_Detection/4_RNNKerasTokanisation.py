from tensorflow.keras.preprocessing.text import Tokenizer

sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentenses)
 
word_index = tokenizer.word_index

for word, index in word_index.items():
    print("Position :", index, ":",word)