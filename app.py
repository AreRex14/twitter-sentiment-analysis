from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

# NLP Packages
from textblob import TextBlob, Word, exceptions
import random
import time

# Malaya NLTK
# import malaya

# multinomial = malaya.multinomial_detect_languages()
# bayes_sentiment = malaya.pretrained_bayes_sentiment()

app = Flask(__name__)
Bootstrap(app)

@app.route('/' , methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    error = ""
    start = time.time()
    if request.method == 'POST': 
        try:
            rawtext = request.form['rawtext']
            # lang_predict = multinomial.predict(rawtext)
            blob = TextBlob(rawtext)
            blob_lang = blob.detect_language()
            # if lang_predict != 'ENGLISH':
            #   en_blob = blob.translate(to='en')
            # else:
            #   en_blob = blob
            if blob_lang != 'en':
               en_blob = blob.translate(to='en')

            pass
        except exceptions.NotTranslated as NT:
            error = NT
        except exceptions.TranslatorError as TE:
            error = TE
        else:
				    # NLP stuff
            blob_sentiment, blob_subjectivity = en_blob.sentiment.polarity, en_blob.sentiment.subjectivity
            number_of_tokens = len(list(en_blob.words))
            
            # if lang_predict == 'MALAY':
            #   malaya_sentiment = bayes_sentiment.predict(rawtext)
            #   malaya_proba = bayes_sentiment.predict(rawtext, get_proba=True)
            #   proba_value = malaya_proba.get(malaya_sentiment)
				    # Extracting Main Points
            nouns = list()
            for word, tag in en_blob.tags:
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
            # fix malaya sentiment not working
            # if lang_predict == 'MALAY':
            #   return render_template('index.html',  status = error, received_text = rawtext, number_of_tokens = number_of_tokens, blob_sentiment = proba_value, blob_subjectivity = blob_subjectivity, summary = summary, final_time = final_time)
            # else:
            return render_template('index.html', status = error, received_text = rawtext, number_of_tokens = number_of_tokens, blob_sentiment = blob_sentiment, blob_subjectivity = blob_subjectivity, summary = summary, final_time = final_time)
            pass
            
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

# handle http error 503 problem, problem might come from python urllib, requests or textblob
# deactivate anything that would disturb the connection/request, antivirus, firewall and so on