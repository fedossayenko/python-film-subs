# f = open('OpenSubtitles.en-uk.en')

# w = open("ukr-eng.csv", "w")

# i = 1
# for x in f:
#     insert = [str(i),str(x.replace('\"', '\''))]
#     i = i + 1
#     w.write(",".join(insert))

# f.close()
# w.close()


# f = open('OpenSubtitles.en-uk.ids')


# w = open("ukr-eng-ids.csv", "w")

# i = 1
# w.write("row, imdb_id\n")
# for x in f:
#     parts = x.split('\n')[0]
#     parts = parts.split('	')
#     # insert = [str(i),str(x.replace('\"', '\''))]
#     imdb_id = parts[0].split('/')[2]
#     a = [str(i), str(imdb_id)]
#     # print(a)
#     i = i+1
#     w.write(",".join(a) + '\n')

# f.close()
# w.close()

ids = open('OpenSubtitles.en-uk.ids')
eng = open('OpenSubtitles.en-uk.en')
ukr = open('OpenSubtitles.en-uk.uk')

w = open("ukr-eng.csv", "w")

w.write("imdb_id, eng_text, second_text, row\n")
for x in ids:
    e = eng.readline().split('\n')[0].replace('\"', '\'').replace(',', '\\')
    u = ukr.readline().split('\n')[0].replace('\"', '\'').replace(',', '\\')

    imdb_id = x.split('/')[2]
    for y in x.split('\t')[2].split(' '):

        a = [str(imdb_id), e, u, str(y)]
        # print(a)
        w.write(",".join(a) + '\n')
