import csv
from textblob import TextBlob, Word, exceptions
import random
import time

# to handle urllib and socket exceptions
import urllib
import socket

import malaya

bayes_sentiment = malaya.pretrained_bayes_sentiment()

filename = ''
filename2 = ''

def analyze_querydata(read_file, write_file):
    count = 0
    msg = ""
    error = ""
    start = time.time()

    filename = read_file
    filename2 = write_file

    alltweets = csv.reader(open(filename, 'r'))

    with open(filename2, 'w', newline='') as analyzetweets:
        writer = csv.writer(analyzetweets)
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            try:
                time_created = row[0]
                tweet_string = row[1]
                tweet_blob = TextBlob(tweet_string)
                tweet_lang = tweet_blob.detect_language()
            except urllib.error.URLError as urlE:
                error = urlE
                print(error)
            except socket.timeout as socketE:
                error = socketE
                print(error)
            except exceptions.NotTranslated as NT:
                error = NT
                print(error)
            except exceptions.TranslatorError as TE:
                error = TE
                print(error)
            else:
            # finally: 
                msg = 'pass'
                # using Malaya for Malay lang tweet
                if tweet_lang == 'ms':
                   malaya_sentiment = bayes_sentiment.predict(tweet_string)
                   malaya_proba = bayes_sentiment.predict(tweet_string, get_proba=True)
                   proba_value = malaya_proba.get(malaya_sentiment)

                   # writer.writerow([count, msg, time_created, tweet_string, number_of_tokens, blob_words, malaya_sentiment, proba_value, blob_subjectivity, summary, final_time])
                   writer.writerow([count, msg, time_created, tweet_string, malaya_sentiment, proba_value])
                 # using textBlob for English lang tweet
                elif tweet_lang == 'en':           
                   tweet_polarity = tweet_blob.sentiment.polarity
                   tweet_sentiment = ''
                
                   if tweet_polarity > 0:
                      tweet_sentiment = 'positive'
                   elif tweet_polarity < 0:
                      tweet_sentiment = 'negative'
                   elif tweet_polarity == 0.0:
                      tweet_sentiment = 'neutral'

                   writer.writerow([count, msg, time_created, tweet_string, tweet_sentiment, tweet_polarity])
                else:
                   msg = 'tweet language is mixed'
                   writer.writerow([count, msg, time_created, tweet_string, '', '',])

    analyzetweets.close()
    print("Done building tweets sentiment!")
			
if __name__ == '__main__':

    print("This python script will calculate the sentiment for each tweet.")
    # need to handle other user io operations(file not existed, or not extensions and else...)
    confirmation = input("Executing this script will overwrite existing data in file if the operation has been done before, proceed with caution. y/n: ")
    if confirmation == 'y':
        read_file = input("Please input a csv file to read tweets from: ")

        analyze_querydata('search-data/'+read_file, 'search-data/sentiment'+read_file)
    else:
        print("You said no. Thank you")
