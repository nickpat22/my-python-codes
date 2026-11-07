from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentenses)

sequences = tokenizer.texts_to_sequences(sentenses)

print("Orignal Sequences:")
for sequence in sequences:
    print(sequence,"Length : ", len(sequence))
    print("--------------------------------------")

print("All Sequences Are of Diffrent Lengths")

max_length = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen = max_length,
    padding = "pre"
)

for sentence, sequence, padded in zip(sequences, sequences,padded_sequences):
    print("Sentence :",sentence)
    print("Orignal sequence :",sequence)
    print("Padeed Sequence:",padded)