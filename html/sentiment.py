from textblob import TextBlob
import json

import sys

print("number of arguments:", len(sys.argv), "arguments")
print("argument list:", str(sys.argv))

class sentiment:

    def getSentiment(sys.argv[1]):
                
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
        avg_sent = total_sent / sentence_count
        fn.append(avg_sent)
        final = json.dumps(fn, indent=2)

        return final
    
    with open("sent_test.txt", "r+") as f:
        fread = f.read()

    this = getSentiment(fread)
    print(this)
