from textblob import TextBlob
import json

class sentiment:
    
    def getSentiment(text):

        sentence_count = 0
        total_sent = 0

        blob = TextBlob(text)
        sentiment_list = []
        word_list = []
        
        for sentence in blob.sentences:
            sent = round(sentence.sentiment.polarity, 3)
            total_sent += sent
            sentence_count += 1
            sentiment_list.append(sent)
            word_count = 0
            i = " "
            words = sentence.split(" ")
            for i in words:
                word_count += 1
            word_list.append(word_count)
                
        fn = list(zip(word_list, sentiment_list))
        final = json.dumps(fn, indent=2)

        avg_sent = total_sent / sentence_count

        return final
    
    with open("bernie.txt", "r+") as f:
        fread = f.read()

    this = getSentiment(fread)
    print(this)

    
    






