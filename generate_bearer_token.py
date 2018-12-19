from searchtweets import load_credentials

credentials_list = load_credentials(filename="./twitter_keys.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)

print(credentials_list)