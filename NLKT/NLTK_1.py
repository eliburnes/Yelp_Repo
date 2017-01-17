#some code from https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors

import nltk
import json
import numpy as np
from nltk.corpus import stopwords
import re
import pickle


test_reviews=[]
test_ratings=[]

train_reviews=[]
train_ratings=[]

x=0
num_load=1000000

with open('/Users/Eli/Desktop/reviews.json') as data_file:    # with handles closing file
    for x in range(num_load):
        jsonObject=json.loads(data_file.readline())
        rating_string=jsonObject['stars']
        # review_string=jsonObject['text']
        #
        # for char in review_string:
        #     if char == ("\n") or char == ("n\\' ") or char == ("\\") or char == ("\\'"):
        #         review_string=review_string.replace(char,'')
        # a=review_string
        if (x < num_load / 2):
            # train_reviews.append(a)
            train_ratings.append(rating_string)
            x=x+1
        if (x>num_load / 2):
            # test_reviews.append(a)
            test_ratings.append(rating_string)
            x = x + 1
        if x%10000==0:
            print x

# print test_reviews
# print train_reviews


def review_to_words(review):
        letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                       review)  # The text to search
        lower_case = letters_only.lower()  # Convert to lower case
        words = lower_case.split()  # Split into words
        stops = set(stopwords.words("english"))
        meaningful_words = [w for w in words if not w in stops]
        return (" ".join(meaningful_words))
'''

print "cleaning train reviews"
clean_train_reviews = []
for review in train_reviews:
    clean_train_reviews.append(review_to_words(review))
print "cleaning test reviews"
clean_test_reviews = []
for review in test_reviews:
    clean_test_reviews.append(review_to_words(review))




print "dumped reviews"


'''

with open('ratingsTrain.pickle', 'wb') as f: # "wb" write bytes
    pickle.dump(train_ratings, f)#dumps classifier

with open('ratingsTest.pickle', 'wb') as f:  # "wb" write bytes
    pickle.dump(test_ratings, f)  # dumps classifier

    print "dumped ratings"
