from pymongo import MongoClient

client = MongoClient(port=27017)
db=client.mean

types = ['adj.', 'adv.', 'v.', 'n.', 'conj.', 'number', 'prep.', 'exclam.', 'pron.', 'det.']
diffs = ['A1', 'A2', 'B1', 'B2', 'C1']
words = []
additionalTypes = {
    'adj.': 'JJ',
    'adv.': 'RB',
    'v.': 'VB',
    'n.': 'NN',
    'prep.': 'IN',
    'conj.': 'CC',
    'pron.': 'PR',
    'det.': 'DT'
}

def add_obj(word, type, diff):
    additional_type = additionalTypes.get(type)
    word = {
        'word': word,
        'type': type,
        'diff': diff,
        'additional_type': additional_type
    }

    words.append(word)
    print(word)
    # db.word_oxford.insert_one(word)

with open('words3000.txt') as word_file:
    lines = word_file.read().split('\n')
    for l in lines:
        parts = l.replace('/', ' ').split(' ')
        prevSelTypes = []
        selTypes = []
        word = parts[0].lower()
        lastType = False
        for x in parts[1:]:
            without_last = x[0:-1]
            if (x in types):
                selTypes.append(x)
            elif without_last in types:
                selTypes.append(without_last)
            elif (x in diffs) and (len(selTypes) > 0 or len(prevSelTypes) > 0):
                if (len(selTypes) == 0):
                    selTypes = prevSelTypes
                for y in selTypes:
                    add_obj(word, y, x)
                prevSelTypes = selTypes
                selTypes = []
            elif (without_last in diffs) and (len(selTypes) > 0 or len(prevSelTypes) > 0):
                if (len(selTypes) == 0):
                    selTypes = prevSelTypes
                for y in selTypes:
                    add_obj(word, y, without_last)
                prevSelTypes = selTypes
                selTypes = []
            else:
                print(parts)
           
        
print(len(words))