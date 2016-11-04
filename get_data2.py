import json

a1=[]

# with open('spotify_dump.json') as data_file:    # with handles closing file
#     data = json.load(data_file)
with open('/Users/Eli/Desktop/reviews.json') as data_file:    # with handles closing file
    for review in data_file:
        jsonObject=json.load(review)
        a1.append(jsonObject)

reviews=[]
ratings=[]

print a1[20]