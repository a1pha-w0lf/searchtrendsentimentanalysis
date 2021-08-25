from googlesearch import search
from textblob import TextBlob
from newspaper import Article
from newspaper import Config
num_page = 3

def sentiment(keyword):
    
    stop = 10
    search_results = search(keyword, stop=stop)
    #print(search_results)
    urls = []
    for url in search_results:
        urls.append(url)

    #Get the article
    overall_sentiment = 0
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    config = Config()

    config.browser_user_agent = user_agent
    config.request_timeout = 40

    for url in urls:
        #print(url)
        article = Article(url, config=config)
        article
        # NLP 
        try:
            article.download()
            article.parse()
            article.nlp()
            # Get the summary of the article
            text = article.summary
            #print(text)
            # Create a TextBlob object
            obj = TextBlob(text)

            #This returns a value between -1 and 1
            sentiment = obj.sentiment.polarity
            #print(sentiment)
            overall_sentiment += sentiment
        except:
            pass

        
    overall_sentiment /= stop
    print(overall_sentiment)

    if overall_sentiment ==0:
        return 
    elif overall_sentiment > 0.11:
        return 1
    else:
        return 0

