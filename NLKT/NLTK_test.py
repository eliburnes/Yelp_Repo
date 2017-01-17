import pickle

numload=2000

pickle_in=open('cleanTest.pickle','rb') # "rb" read bytes
clean_test_reviews_big=pickle.load(pickle_in)

pickle_in=open('ratingsTest.pickle','rb') # "rb" read bytes
test_ratings_big=pickle.load(pickle_in)

test_ratings=test_ratings_big[:numload]
clean_test_reviews=clean_test_reviews_big[:numload]


pickle_in= open('random_forest.pickle', 'rb')  # "rb" read bytes
forest = pickle.load(pickle_in)

pickle_in = open('vectorizer.pickle', 'rb')  # "rb" read bytes
vectorizer = pickle.load(pickle_in)

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
