# kuis-twitter-sentiment-analysis

This project has two parts:
1. Cli operation that write or both read and write to/from a csv file for standard(free), 30 day(premium sandbox) and full archive(premium sandbox) Twitter Search API endpoints
2. A NLP Flask app that visualize sentiments of 30 day and full archive and has a section where paragraphs of strings(tweet or else) can be input and output several informations(sentiment, subjectivity, ...) regarding the strings inserted

This project basically uses _Tweepy_ to access standard search API and [_TwitterDev/search-tweets-python_](https://github.com/twitterdev/search-tweets-python) to access premium search API endpoint and retrieve tweets and _TextBlob_ and _Malaya_ for NLP purpose.

Refer to [wiki](https://github.com/AreRex14/kuis-twitter-sentiment-analysis/wiki) to set up.
