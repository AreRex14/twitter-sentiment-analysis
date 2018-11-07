from config import api
import tweepy
import csv
import time

# to handle regex
import re

# need to handle blank separator row

# malay language toolkit
import malaya

# global variables to be used by user defined functions
filename = ""
filename2 = ""

# 1. collecting data
#Put your search term
def get_querydata(query, named_file):
    searchquery = query
    tweets = tweepy.Cursor(api.search,q=searchquery,count=5000,locale='ms').items()

    count = 0
    errorCount= 0
    msg = ""
    filename = named_file
    # edit to create a new file if not exist without messing with the writer pointer
    with open(filename, 'a', newline='') as alltweets: 
        writer = csv.writer(alltweets)
        while True:
            try:
                tweet = next(tweets)
                count += 1
                # use count-break during dev to avoid twitter restrictions
                # if (count >= 5000):
                    # break
            except tweepy.TweepError:
                #catches TweepError when rate limiting occurs, sleeps, then restarts.
                #nominally 15 minnutes, make a bit longer to avoid attention.
                msg = "sleeping...."
                print(msg)
                time.sleep(60*16)
                tweet = next(tweets)
            except StopIteration:
                break
            try:
                msg = "Writing to CSV tweet number:"+str(count)
                print(msg)
                writer.writerow([tweet.created_at, tweet.text])  
            except UnicodeEncodeError:
                errorCount += 1
                msg = "UnicodeEncodeError,errorCount ="+str(errorCount)
                print(msg)

    msg = "completed, errorCount ="+str(errorCount)+" total tweets="+ str(count)
    print(msg)

def clean_data(read_file, write_file):

    count = 0
    errorCount= 0
    msg = ""

    filename = read_file
    filename2 = write_file

    alltweets = csv.reader(open(filename, 'r'))
    # n = sum(1 for line in csv.reader(filename)) # not working
    # print(str(n))

    
    with open(filename2, 'w', newline='') as cleantweets:
        writer = csv.writer(cleantweets)
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            cleanTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", row[1]).split())
            writer.writerow([row[0], cleanTweet])
            # if count == n:
            #    break
    cleantweets.close()
    print('Done cleaning tweets!')

# read clean tweets file and write to normalized tweets file
def normalize_string(read_file, write_file):
    count = 0
    errorCount= 0
    msg = ""
    filename = read_file
    filename2 = write_file

    alltweets = csv.reader(open(filename, 'r', encoding="utf8", errors='ignore'))

    multinomial = malaya.multinomial_detect_languages()

    with open(filename2, 'w', newline='') as normalizedtweets:
        writer = csv.writer(normalizedtweets)
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            lang_predict = multinomial.predict(row[1])
            if lang_predict == 'MALAY':
               normalized_tweet = malaya.basic_normalizer(row[1])
               writer.writerow([row[0], normalized_tweet])
            else:
               writer.writerow([row[0], row[1]])
    normalizedtweets.close()
    print('Done normalizing tweets!')

def remove_duplicate(read_file, write_file):
    errorCount= 0
    msg = ""
    filename = read_file
    filename2 = write_file

    alltweets = csv.reader(open(read_file, 'r'))
    noDup = csv.writer(open(write_file, 'w'))

    tweets = set()
    i = 0
	# add exception handling
    for row in alltweets:
        i = i + 1
        # print i
        if row[1] not in tweets:
           t = row[1].lower()
           t = t.replace('\n', '')
           noDup.writerow([row[0], t])
           # print "writing row..."
           tweets.add(row[1])

    print('Done removing duplicated tweets!')

if __name__ == '__main__':
    
    '''    
    file = open('hashtags-keywords.txt', 'r') # contains a list of keywords to search and retrieve tweets
    queries = file.readlines()

    # execute below scripts will run again the operations and overwrite existing files
    print('Getting tweets data based on keywords file...')
    for q in queries:
        # read one keyword at a time
        print("----")
        get_querydata(q, 'search-data/searchTweets.csv') # comment in when not in used
    '''

    print('Removing duplicated tweets...')
    remove_duplicate('search-data/searchTweets.csv', 'search-data/uniqueSearchTweets.csv') # comment in when not in used

    print('Cleaning tweets...')
    clean_data('search-data/uniqueSearchTweets.csv', 'search-data/cleanSearchTweets.csv') # comment in when not in used

    print('Normalizing tweets...')
    normalize_string('search-data/cleanSearchTweets.csv', 'search-data/normalizedSearchTweets.csv') # comment in when not in used