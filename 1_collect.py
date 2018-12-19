import csv
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

def get_querydata(query, from_date, to_date, write_file):
    premium_search_args = load_credentials("./twitter_keys.yaml",
                                          yaml_key="search_tweets_fullarchive_prod",
                                          env_overwrite=False)
    count = 0
    errorCount= 0
    msg = ""


    rule = gen_rule_payload(query,
                        from_date=from_date,
                        to_date=to_date,
                        results_per_call=20)
    print(rule)

    tweets = collect_results(rule, max_results=20, result_stream_args=premium_search_args)
    tweets = iter(tweets)

    with open(write_file, 'a', newline='') as alltweets: # refactor to just append to new line rather than writing to new file
        writer = csv.writer(alltweets)
        while True:
            try:
                tweet = next(tweets)
                count += 1
                # use count-break during dev to avoid twitter restrictions
                if (count > 20):
                   break
            # need to handle other exceptions throw by twitter api wrapper
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

    print("This python script will collect full archive(sandbox) tweets data from endpoint")

    # need to handle other user io operations(file not existed, or not extensions and else...)
    confirmation = input("Executing this script will overwrite existing data in file if the operation has been done before, proceed with caution. y/n: ")
    if confirmation == 'y' or confirmation == 'Y':
        from_date = input('Please input a from date of tweets to gather: yyyy-mm-dd')
        to_date = input('Please input a to date of tweets to gather: yyyy-mm-dd')
        write_file = input('Please input a csv file to write tweets data to: ')
             
        file = open('./queries.txt', 'r') # contains a list of keywords to search and retrieve tweets
        queries = file.readlines()
        line_count = 0
        # execute below scripts will run again the operations and overwrite existing data in file
        
        print('Getting tweets data based on keywords file...')
        for q in queries:
            line_count += 1
            if line_count > 4: # need to implement this temporarily since sandbox is rate limited, less requests can be made
                break
            # read one keyword at a time
            print("----")
            # get_querydata(search_type, q, './search-data/'+write_file)
            get_querydata(q, from_date, to_date, './search-data/'+write_file)
    elif confirmation == 'n' or confirmation == 'N':
        print("You said no. Thank you")
    else:
        print('Invalid option/answer!')
