'''
compute total, positive, negative and neutral tweets
'''

import csv

def getStats(fileRead, fileWrite):
    fileRead = csv.reader(open(fileRead, "r"))

    tot = 0
    pos = 0
    neg = 0
    neu = 0

    for row in fileRead:
        tot = tot + 1;
        if row[6] == "positive":
            pos = pos + 1
        elif row[6] == "negative":
            neg = neg + 1
        elif row[6] == "neutral":
            neu = neu + 1

    print("total tweets: ", tot)
    print("Tweets stat: ")
    print("positive: ", pos)
    print("negative: ", neg)
    print("neutral: ", neu)

    results = csv.writer(open(fileWrite, "w"))
    results.writerow(['TextBlob/Malaya computed sentiments result'])
    results.writerow(['Total', 'Positive', 'Negative', 'Neutral'])
    results.writerow([tot, pos, neg, neu])

if __name__ == '__main__':
    print('7 day standard search tweets: ')
    getStats('../search-data/standardSearchTweetsSentiment.csv', '../search-data/standardComputedResults.csv')