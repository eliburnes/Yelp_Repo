import fasttext

print "hi"
# CBOW model
model = fasttext.cbow('train2.txt', 'model')
print model.words # list of words in dictionary
