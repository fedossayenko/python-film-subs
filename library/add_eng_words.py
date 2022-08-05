from pymongo import MongoClient
from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=client.mean


with open('noun.txt') as word_file:
    lines = word_file.read().split('\n')
    for l in lines:
        parts = l.split('|')

        items = parts[0].split(' ')
        # print(items)
        # print(parts[1])

        insert_word = {
            'text': items[4],
            'id': items[0],
            'secondary_id': items[1],
            'word_type': items[2],
            'one_more_id': items[3],
            'description': parts[1]

        }
        # print(insert_word)
        result=db.word.insert_one(insert_word)
print('Done')