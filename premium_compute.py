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
    results.writerow(['TextBlob and Malaya computed sentiments result'])
    results.writerow(['Total', 'Positive', 'Negative', 'Neutral'])
    results.writerow([tot, pos, neg, neu])

if __name__ == '__main__':
    print('Full archive search tweets: ')
    getStats('search-data/searchTweetsSentiment.csv', 'search-data/computedResults.csv')
    print('30 day search tweets: ')
    getStats('search-data/searchTweetsSentiment30days.csv', 'search-data/computedResults30days.csv')