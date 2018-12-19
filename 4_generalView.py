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
        if row[4] == "positive":
            pos = pos + 1
        elif row[4] == "negative":
            neg = neg + 1
        elif row[4] == "neutral":
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

    print("This python script will generally compute tweets based on sentiment type.")
    # need to handle other user io operations(file not existed, or not extensions and else...)
    confirmation = input("Executing this script will overwrite existing data in file if the operation has been done before, proceed with caution. y/n: ")
    if confirmation == 'y':
        read_file = input("Please input a csv file to read tweets from: ")

        getStats('search-data/'+read_file, 'search-data/computed'+read_file)
    else:
        print("You said no. Thank you")
