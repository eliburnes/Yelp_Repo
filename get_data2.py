import json
import pickle
import csv, codecs, cStringIO, io
import unicodedata
import numpy as np
import fasttext
import codecs

classifier = fasttext.supervised('combined_train.txt', 'model')
# result = classifier.test('combined_test.txt')
# print 'P@1:', result.precision
# print 'R@1:', result.recall
# print 'Number of examples:', result.nexamples
print classifier

reviews = ['amazing food. very good, excellent service','very bad, worst ever, gross']
labels=classifier.predict(reviews)
print labels
print "done"

#
# reviews=[]
# ratings=[]
# x=0
# num_load= 100
#


# with open('/Users/Eli/Desktop/reviews.json') as data_file:    # with handles closing file
#     for review in data_file:
#         if (x<num_load):
#             jsonObject=json.loads(review)
#             rating_string=jsonObject['stars']
#             review_string=jsonObject['text']
#             good_review=unicodedata.normalize('NFKD', review_string).encode('ascii','ignore')
#             a=[good_review]
#             b=[rating_string]
#             reviews.append(a)
#             ratings.append(b)
#             x=x+1
#         if x>num_load:
#             break
#

#write reviews and ratings into csv file
# a=csv.writer(file('ratings_100.csv','wb'),dialect='excel')
# a.writerows(ratings)
#
# w=csv.writer(file('reviews_100.csv','wb'),dialect='excel')
# w.writerows(reviews)

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
# #turn read lists into numpy arrays
# numpy_reviews=np.array(reviews_loaded_initial)
# numpy_ratings_string=np.array(ratings_loaded_initial)
# numpy_ratings= numpy_ratings_string.astype(float)
#
# #make list of reviews with labels
# combined_test=[]
# combined_train=[]
# x=0
# for x in range (len(numpy_reviews)/2):
#     combined_test.append(numpy_reviews.item(x)+"__label__"+str(numpy_ratings.item(x)))
#     x=x+1
#
# for x in range (len(numpy_reviews)/2):
#     combined_train.append(numpy_reviews.item(x)+"__label__"+str(numpy_ratings.item(x)))
#     x=x+1
#
# #save combined list to txt files
# with codecs.open('combined_test.txt',"a","utf-8") as my_file:
#     for element in combined_test:
#         my_file.write(element+"\n")
#
# with codecs.open('combined_train.txt', "a", "utf-8") as my_file:
#     for element in combined_train:
#         my_file.write(element + "\n")
#
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
