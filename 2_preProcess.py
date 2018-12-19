import csv
import time
import re
# need to handle blank separator row
import malaya

def clean_data(read_file, write_file):

    count = 0
    errorCount= 0
    msg = ""

    alltweets = csv.reader(open(read_file, 'r'))
    
    with open(write_file, 'w', newline='') as cleantweets:
        writer = csv.writer(cleantweets)
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            cleanTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", row[1]).split())
            writer.writerow([row[0], cleanTweet, row[2]])
            # if count == n:
            #    break
    cleantweets.close()
    print('Done cleaning tweets!')

def normalize_string(read_file, write_file):
    count = 0
    errorCount= 0
    msg = ""

    alltweets = csv.reader(open(read_file, 'r', encoding="utf8", errors='ignore'))

    multinomial = malaya.multinomial_detect_languages()

    with open(write_file, 'w', newline='') as normalizedtweets:
        writer = csv.writer(normalizedtweets)
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            lang_predict = multinomial.predict(row[1])
            if lang_predict == 'MALAY':
               normalized_tweet = malaya.basic_normalizer(row[1])
               writer.writerow([row[0], normalized_tweet, row[2]])
            else:
               writer.writerow([row[0], row[1], row[2]])
    normalizedtweets.close()
    print('Done normalizing tweets!')

def remove_duplicate(read_file, write_file):
    errorCount= 0
    msg = ""

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
           noDup.writerow([row[0], t, row[2]])
           # print "writing row..."
           tweets.add(row[1])

    print('Done removing duplicated tweets!')

if __name__ == '__main__':

    print("This python script will remove duplicated tweets, cleaning tweets and normalizing tweets.")
    # need to handle other user io operations(file not existed, or not extensions and else...)
    confirmation = input("Executing this script will overwrite existing data in file if the operation has been done before, proceed with caution. y/n: ")
    if confirmation == 'y':
        read_file = input("Please input a csv file to read tweets from: ")

        remove_duplicate('search-data/'+read_file, 'search-data/unique'+read_file)
        clean_data('search-data/unique'+read_file, 'search-data/clean'+read_file) 
        normalize_string('search-data/clean'+read_file, 'search-data/normalized'+read_file) 
    else:
        print("You said no. Thank you")
	
