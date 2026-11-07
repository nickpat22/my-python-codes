from tensorflow.keras.preprocessing.text import Tokenizer

sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentenses)

sequences = tokenizer.texts_to_sequences(sentenses)

for sentence, sequence in zip(sentenses, sequences):
    print("Sentence :", sentence)
    print("Sequence :", sequence)
    print("------------------------------------")