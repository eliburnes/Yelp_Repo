import json
import pickle
import csv, codecs, cStringIO, io
import unicodedata
import numpy as np
import fasttext
import codecs
# #

#
# a =  "\\ hellow how are you m8"
# b=a.replace("\\","")
# print b


reviews=[]
ratings=[]
x=0
num_load= 1000



with open('/Users/Eli/Desktop/reviews.json') as data_file:    # with handles closing file
    for review in data_file:
        if (x<num_load):
            jsonObject=json.loads(review)
            rating_string=jsonObject['stars']
            review_string=jsonObject['text']

            for char in review_string:
                if char == ("\n") or char == ("n\\' ") or char == ("\\") or char == ("\\'"):
                    review_string=review_string.replace(char,'')

            # second_review=review_string.replace("\\","84993")
            ##fourth_review=unicodedata.normalize('NFKD', unicode(third_review)).encode('ascii','ignore')
            a=[review_string]

            reviews.append(a)
            ratings.append(rating_string)
            x=x+1
        if x>num_load:
            break

print reviews
print ratings




#write reviews and ratings into csv file
# a=csv.writer(file('ratings_100.csv','wb'),dialect='excel')
# a.writerows(ratings)
#
# w=csv.writer(file('reviews_100.csv','wb'),dialect='excel')
# w.writerows(reviews)
#
# #load reviews and ratings from csv files
# reviews_loaded_initial=[]
# with open('reviews_100.csv', 'Un') as csvfile:
#     c=csv.reader(csvfile)
#     for row in c:
#         reviews_loaded_initial.append(','.join(row))
# ratings_loaded_initial=[]
# with open('ratings_100.csv', 'rb') as csvfile:
#     a=csv.reader(csvfile)
#     for row in a:
#         ratings_loaded_initial.append(','.join(row))
#

#turn read lists into numpy arrays
numpy_reviews=np.array(reviews)
numpy_ratings_string=np.array(ratings)
# numpy_ratings= numpy_ratings_string.astype(float)

#make list of reviews with labels
combined_test=[]
combined_train=[]
manual_test=[]

for x in range (len(numpy_reviews)/2):
    combined_train.append("__label__" + str(ratings[x]) + " , " + numpy_reviews.item(x))

# for x in range (len(numpy_reviews)/2):
#     x=x+len(numpy_reviews)/2
#     combined_test.append("__label__"+str(ratings[x])+" , "+numpy_reviews.item(x))

for x in range (len(numpy_reviews)/2):
    x=x+len(numpy_reviews)/2
    combined_test.append(numpy_reviews.item(x))



for x in range (len(numpy_reviews)/2):
    x=x+len(numpy_reviews)/2
    manual_test.append(numpy_reviews.item(x))


# save combined list to txt files
with codecs.open('combined_test.txt', "a", "utf-8") as my_file:
    for element in combined_test:
        my_file.write(element + "\n")

with codecs.open('combined_train.txt', "a", "utf-8") as my_file:
    for element in combined_train:
        my_file.write(element + "\n")

with codecs.open('manual_test.txt', "a", "utf-8") as my_file:
    for element in manual_test:
        my_file.write(element + "\n")


# classifier = fasttext.supervised('combined_train.txt', 'model')

# result = classifier.test('combined_test.txt',k=5)
# print 'P@1:', result.precision
# print 'R@1:', result.recall
# print 'Number of examples:', result.nexamples
# print classifier

# reviews2=[]
#
# with open('combined_train.txt') as data:
#      reviews2=data.read()
#
#
# with open('combined_test.txt') as data:
#     reviews=data.read()
#
# labels=classifier.predict(reviews)
# print labels
#
#
#



##turn labels into one hot vectors
# one_hot_vectors=[]
# for rating in numpy_ratings:
#     a=[0,0,0,0,0]
#     a[int(rating-1)]=a[int(rating-1)]+1
#     one_hot_vectors.append(a)
# print one_hot_vectors
#
#
#


# with open('ratings.pickle', 'wb') as f: # "wb" write bytes
#     pickle.dump(ratings, f)#dumps labels
#
# with open('reviews.pickle', 'wb') as f:  # "wb" write bytes
#     pickle.dump(reviews, f)  #dumps features classifier