import nltk
import json
import numpy as np
from nltk.corpus import stopwords
import re
import pickle

numload=500000

pickle_in=open('cleanTrain.pickle','rb') # "rb" read bytes
clean_train_reviews_big=pickle.load(pickle_in)

pickle_in=open('ratingsTrain.pickle','rb') # "rb" read bytes
train_ratings_big=pickle.load(pickle_in)

print "loaded all train array pickles...shortening arrays"

clean_train_reviews=clean_train_reviews_big[:numload]

train_ratings=train_ratings_big[:numload]

print "shortened train arrays..."

print "Creating the bag of words...\n"
from sklearn.feature_extraction.text import CountVectorizer
# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)
# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)
# Numpy arrays are easy to work with, so convert the result to an
# array
train_data_features = train_data_features.toarray()


print "Training the random forest..."
from sklearn.ensemble import RandomForestClassifier
# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100)

# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit(train_data_features, train_ratings)

print "dump random forest and vectorizer"


with open('random_forest.pickle', 'wb') as f: # "wb" write bytes
    pickle.dump(forest, f)#dumps classifier


with open('vectorizer.pickle', 'wb') as f: # "wb" write bytes
    pickle.dump(vectorizer, f)#dumps classifier
