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
            writer.writerow([row[0], cleanTweet, row[2]])
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
               writer.writerow([row[0], normalized_tweet, row[2]])
            else:
               writer.writerow([row[0], row[1], row[2]])
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
           noDup.writerow([row[0], t, row[2]])
           # print "writing row..."
           tweets.add(row[1])

    print('Done removing duplicated tweets!')

if __name__ == '__main__':

    print('Full archive tweets operations...')
    print('Removing duplicated tweets...')
    remove_duplicate('search-data/searchTweets.csv', 'search-data/uniqueSearchTweets.csv') # comment in when not in used

    print('Cleaning tweets...')
    clean_data('search-data/uniqueSearchTweets.csv', 'search-data/cleanSearchTweets.csv') # comment in when not in used

    print('Normalizing tweets...')
    normalize_string('search-data/cleanSearchTweets.csv', 'search-data/normalizedSearchTweets.csv') # comment in when not in used

    print('30 day tweets operations...')
    print('Removing duplicated tweets...')
    remove_duplicate('search-data/searchTweets30days.csv', 'search-data/uniqueSearchTweets30days.csv') # comment in when not in used

    print('Cleaning tweets...')
    clean_data('search-data/uniqueSearchTweets30days.csv', 'search-data/cleanSearchTweets30days.csv') # comment in when not in used

    print('Normalizing tweets...')
    normalize_string('search-data/cleanSearchTweets30days.csv', 'search-data/normalizedSearchTweets30days.csv') # comment in when not in used