#########################################################
## Step 1 : Import required Labruries
#########################################################

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

#########################################################
## Step 2 : Configruation of values
#########################################################


VOCAB_SIZE = 10000 #Comsider most frequent 10000 unique words
MAX_LEARN = 200    #Consider max 200 words in review

#########################################################
# STep 3 : Load the imdb databse #Internet Movie Database
#########################################################

print("-"*40)

print("Movie Sentiment Analysis using LSTM")

print("-"*40)

print("Loading the Dataset")

(X_train,Y_train), (X_test,Y_test) = imdb.load_data(num_words = VOCAB_SIZE)

print("IMDB Dataset Loaded Successfully")

print("Number of Training Reviews : ",len(X_train))
print("Number of Testing Reviews : ",len(X_test))

#########################################################
# X_train   Revieves used for training
# Y_Train   Actual Sentimants of training
# X_test    Revieves used for Testing
# Y_test    Actual Sentiment of training
#Sentiments:
    #0: Negitive
    #1: Positive Sentiment
#########################################################

#########################################################
# Step 4 : Load the word Distonary
#########################################################

word_index = imdb.get_word_index()

#Distonary Contains mapping of words and its corresponding numbers
# Drishum is good movie     -> (20 56 78 43)
# 20 -> Drishium
# 56 -> is
# 78 -> good
# 43 -> movie


#########################################################
# Step 5 : Create Reverse Distonary
#########################################################

reverse_word_index = {}

for word,index in word_index.items():
    reverse_word_index[index+3] = word

