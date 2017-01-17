import json
import pickle
import csv, codecs, cStringIO, io
import unicodedata
import numpy as np
import fasttext
import codecs
# #



reviews=[]
ratings=[]
x=0
num_load= 200



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
