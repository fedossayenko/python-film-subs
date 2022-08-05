# f = open('subtitles_all.txt')
f = open('subtitles_month.txt')

w = open("subtitles_all.csv", "w")


for x in f:
    parts = x.split('\t')
    link = parts[-1].split('\n')[0]
    link_part = link.split('/')
    if ('10648342' in x):
        # print(parts)
        if (link != 'URL' and len(link_part) > 1):
            link = link_part[4]+ '/' + link_part[5]
        if (len(link_part) > 1):
            if (parts[4] == 'en' or parts[4] == 'ru' or parts[4] == 'ISO639'):
                arr = [
                    parts[4],
                    parts[6],
                    parts[7],
                    parts[8],
                    link
                ]
                print(arr)
                # w.write(','.join(arr) + '\n')
        else:
            print(parts)

f.close()
# w.close()