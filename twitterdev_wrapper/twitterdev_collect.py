import csv
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

'''
premium_search_args = load_credentials("./twitter_keys.yaml",
                                       yaml_key="search_tweets_fullarchive_dev",
                                       env_overwrite=False)
'''

premium_search_args = load_credentials("./twitter_keys.yaml",
                                       yaml_key="search_tweets_30day_dev",
                                       env_overwrite=False)

filename = ""

def get_querydata(query, write_file):
    count = 0
    errorCount= 0
    msg = ""
    filename = write_file
    searchquery = query

    '''
    rule = gen_rule_payload(searchquery,
                        from_date="2018-01-01", #UTC 2018-10-01 00:00
                        to_date="2018-10-31",#UTC 2018-10-30 00:00
                        results_per_call=30)
    '''

    rule = gen_rule_payload(searchquery,
                        results_per_call=30)
    print(rule)

    tweets = collect_results(rule, max_results=30, result_stream_args=premium_search_args)
    tweets = iter(tweets)

    with open(filename, 'a', newline='') as alltweets: 
        writer = csv.writer(alltweets)
        while True:
            try:
                tweet = next(tweets)
                count += 1
                # use count-break during dev to avoid twitter restrictions
                if (count > 30):
                   break
            # need to handle other exceptions throw by twitterdev api wrapper
            except StopIteration:
                break
            try:
                print("Writing to CSV tweet number:"+str(count))
                writer.writerow([tweet.created_at_datetime, tweet.text, tweet.generator.get("name")])  
            except UnicodeEncodeError:
                errorCount += 1
                print("UnicodeEncodeError,errorCount ="+str(errorCount))

    print("completed, errorCount ="+str(errorCount)+" total tweets="+ str(count))

if __name__ == '__main__':
        
    file = open('../hashtags-keywords.txt', 'r') # contains a list of keywords to search and retrieve tweets
    queries = file.readlines()

    # execute below scripts will run again the operations and overwrite existing files
    print('Getting tweets data based on keywords file...')
    for q in queries:
        # read one keyword at a time
        print("----")
        get_querydata(q, '../search-data/searchTweets30days.csv') # comment in when not in used