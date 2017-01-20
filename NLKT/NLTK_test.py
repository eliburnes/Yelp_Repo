import pickle
import gc

numload=20000

# http://stackoverflow.com/questions/2766685/how-can-i-speed-up-unpickling-large-objects-if-i-have-plenty-of-ram

print "loading test reviews"
pickle_in=open('cleanTest.pickle','rb') # "rb" read bytes
gc.disable()
clean_test_reviews_big=pickle.load(pickle_in)
gc.enable()
pickle_in.close()

print "loading test ratings"
pickle_in_2=open('ratingsTest.pickle','rb') # "rb" read bytes
gc.disable()
test_ratings_big=pickle.load(pickle_in_2)
gc.enable()
pickle_in_2.close()

test_ratings=test_ratings_big[:numload]
clean_test_reviews=clean_test_reviews_big[:numload]

print "loading vectorizer"
pickle_in_4 = open('vectorizer.pickle', 'rb')  # "rb" read bytes
gc.disable()
vectorizer = pickle.load(pickle_in_4)
gc.enable()
pickle_in_4.close()


print "loading forest"
pickle_in_3= open('random_forest.pickle', 'rb')  # "rb" read bytes
gc.disable()
forest = pickle.load(pickle_in_3)
gc.enable()
pickle_in_3.close()



print "done trainting...now testing  test set"

test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)

print "done testing, now calculating accuracy statistics..."

differences = []
differences = result - test_ratings

correct = 0

for x in range(len(result)):
    if int(result[x]) == int(test_ratings[x]):
        correct = correct + 1

print 'correct: ' + str(correct)
print 'total test ratings: ' + str(len(test_ratings))
print '% correct: ' + str(float(correct) / float(len(test_ratings)) * 100)

average_diff = float(sum(differences)) / float(len(differences))

print 'average difference: ' + str(average_diff)
