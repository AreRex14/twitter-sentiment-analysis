# Making decisions informed by KUIS/IIUCS alumni(customer) sentiment

Understand customer sentiment as people and markets respond to product and business decisions. Twitter endpoints and tools enable techniques to analyze and inform next steps based on sentiment. Sentiment analysis can predict the outcome of upcoming events, evaluate the impact of a recent product launch, pivot the direction or content of an ad campaign, and more.

Twitter product involved are Search APIs.There are 3 tiers:
- Standard
- Premium(sandbox or paid)
  - 30 day
  - Full-archive
- Enterprise(paid)

2 tiers that have been experiment/tried are standard and premium(sandbox) both 30 day and full-archive and I have choose to use premium(sandbox) full-archive in this project since it is free and more suitable to gather more tweets from our customer for this project than standard endpoint. This premium endpoint should be consider to be upgrade to premium(paid) or enterprise since they provide more capabilities than sandbox. A more clear view of the comparison between these endpoints can checkout here [search apis endpoint comparison.](https://developer.twitter.com/en/docs/tweets/search/overview)

This project has two parts:
1. Cli operation that write or both read and write to/from a csv file for standard(free), 30 day(premium sandbox) and full archive(premium sandbox) Twitter Search API endpoints
2. A NLP Flask app that visualize sentiments of 30 day and full archive and has a section where paragraphs of strings(tweet or else) can be input and output several informations(sentiment, subjectivity, ...) regarding the strings inserted

This project basically uses _Tweepy_ to access standard search API and [_TwitterDev/search-tweets-python_](https://github.com/twitterdev/search-tweets-python) to access premium search API endpoint and retrieve tweets and _TextBlob_ and _Malaya_ for NLP purpose.

Refer to [wiki](https://github.com/AreRex14/kuis-twitter-sentiment-analysis/wiki) to set up.
