import csv
from textblob import TextBlob, Word, exceptions
import random
import time

# to handle urllib and socket exceptions
import urllib
import socket

# import malay language toolkit and pandas
import malaya

multinomial = malaya.multinomial_detect_languages()
bayes_sentiment = malaya.pretrained_bayes_sentiment()

filename = ''
filename2 = ''
count = 0
    msg = ""
    error = ""

def analyze_querydata(read_file, write_file):

    start = time.time()

    filename = read_file
    filename2 = write_file

    alltweets = csv.reader(open(filename, 'r'))

    with open(filename2, 'w', newline='') as analyzetweets:
        writer = csv.writer(analyzetweets)
        blob_words = set()
        # while True:
        for row in alltweets:
            count = count + 1
            print(str(count))
            try:
                tweet_string = row[1]
                received_text = tweet_string
                lang_predict = multinomial.predict(received_text)
                blob = TextBlob(tweet_string)
                if lang_predict != 'ENGLISH':
                   received_text2 = blob.translate(to='en')
                else:
                   received_text2 = blob

                pass
            except urllib.error.URLError as urlE:
                error = urlE
                print(error)

                received_text = tweet_string
                blob_words = list(blob.words)
                number_of_tokens = len(list(blob.words))
                number_of_tokens = number_of_tokens
                time_created = row[0]

                writer.writerow([count, error, time_created, received_text, number_of_tokens, blob_words])
            except socket.timeout as socketE:
                error = socketE
                print(error)

                received_text = tweet_string
                blob_words = list(blob.words)
                number_of_tokens = len(list(blob.words))
                number_of_tokens = number_of_tokens
                time_created = row[0]

                writer.writerow([count, error, time_created, received_text, number_of_tokens, blob_words])
            except exceptions.NotTranslated as NT:
                error = NT
                print(error)
                received_text = tweet_string
            except exceptions.TranslatorError as TE:
                error = TE
                print(error)
                received_text = tweet_string
            else:
                number_of_tokens = len(list(blob.words))

                # using textBlob for NLP of languages other than Malay
                blob_sentiment, blob_subjectivity = received_text2.sentiment.polarity, received_text2.sentiment.subjectivity
                
                textblob_sentiment = ''
                if blob.sentiment.polarity > 0:
                    textblob_sentiment = 'positive'
                elif blob.sentiment.polarity < 0:
                    textblob_sentiment = 'negative'
                elif blob.sentiment.polarity == 0.0:
                    textblob_sentiment = 'neutral'

                # Extracting Main Points
                nouns = list()
                for word, tag in received_text2.tags:
                    if tag == 'NN':
                        nouns.append(word.lemmatize())
                        len_of_words = len(nouns)
                        rand_words = random.sample(nouns, len(nouns))
                        final_word = list()
                        for item in rand_words:
                            word = Word(item).pluralize()
                            final_word.append(word)
                            summary = final_word
                            end = time.time()
                            final_time = end-start
                            received_text = tweet_string
                            number_of_tokens = number_of_tokens
                            time_created = row[0]
                            blob_words = list(blob.words)
                            blob_sentiment = blob_sentiment
                            blob_subjectivity = blob_subjectivity
                            summary = summary
                            final_time = final_time
                            msg = "pass"
                
                # using Malaya for NLP of Malay lang tweet
                if lang_predict == 'MALAY':
                   malaya_sentiment = bayes_sentiment.predict(received_text)
                   malaya_proba = bayes_sentiment.predict(received_text, get_proba=True)
                   proba_value = malaya_proba.get(malaya_sentiment)

                   writer.writerow([count, msg, time_created, received_text, number_of_tokens, blob_words, malaya_sentiment, proba_value, blob_subjectivity, summary, final_time])
                else:
                   writer.writerow([count, msg, time_created, received_text, number_of_tokens, blob_words, textblob_sentiment, blob_sentiment,blob_subjectivity, summary, final_time])

                pass
    analyzetweets.close()
    print("Done building tweets sentiment!")
			
if __name__ == '__main__':
    print('Processing sentiments for 7 day standard search tweets...')
    analyze_querydata('../search-data/standardNormalizedSearchTweets.csv', '../search-data/standardSearchTweetsSentiment.csv')