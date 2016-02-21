from textblob import TextBlob
import json

import sys

#print("number of arguments:", len(sys.argv), "arguments")
#print("argument list:", str(sys.argv))

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
                
        final = list(zip(word_list, sentiment_list))

        return final

    this = getSentiment(sys.argv[1])

    sents = []
    i = 0
    for i in this:
        sents.append(i[1])

    words = []
    for i in this:
        words.append(i[0])

    durations = []
    for i in words:
        duration = round((i * 0.4),3)
        durations.append(duration)
    

    notes = []

    for i in sents:
        if i < -.85:
            notes.append(["C",0])
        elif i < -.83:
            notes.append(["C#",0])
        elif i < -.80:
            notes.append(["D", 0])
        elif i < -.78:
            notes.append(["D#",0])
        elif i < -.75:
            notes.append(["E",0])
        elif i < -.72:
            notes.append(["F",0])
        elif i < -.69:
            notes.append(["F#",0])
        elif i < -.66:
            notes.append(["G",0])
        elif i < -.63:
            notes.append(["G#",0])
        elif i < -.60:
            notes.append(["A",0])
        elif i < -.59:
            notes.append(["A#",0])
        elif i < -.56:
            notes.append(["B",0])
        elif i < -.53:
            notes.append(["C",1])
        elif i < -.50:
            notes.append(["C#",1])
        elif i < -.46:
            notes.append(["D",1])
        elif i < -.42:
            notes.append(["D#",1])
        elif i < -.39:
            notes.append(["E",1])
        elif i < -.30:
            notes.append(["F",1])
        elif i < -.25:
            notes.append(["F#",1])
        elif i < -.21:
            notes.append(["G",1])
        elif i < -.19:
            notes.append(["G#",1])
        elif i < -.15:
            notes.append(["A",1])
        elif i < -.13:
            notes.append(["A#",1])
        elif i < -.10:
            notes.append(["B",1])
        elif i < -.05:
            notes.append(["C",2])
        elif i < 0:
            notes.append(["C#",2])
        elif i < .05:
            notes.append(["D",2])
        elif i < .08:
            notes.append(["D#",2])
        elif i < .12:
            notes.append(["E",2])
        elif i < .17:
            notes.append(["F",2])
        elif i < .20:
            notes.append(["G",2])
        elif i < .23:
            notes.append(["G#",2])
        elif i < .27:
            notes.append(["A",2])
        elif i < .33:
            notes.append(["A#",2])
        elif i < .38:
            notes.append(["B",2])
        elif i < .40:
            notes.append(["C",3])
        elif i < .43:
            notes.append(["C#",3])
        elif i < .47:
            notes.append(["D",3])
        elif i < .52:
            notes.append(["D#",3])
        elif i < .56:
            notes.append(["E",3])
        elif i < .59:
            notes.append(["F",3])
        elif i < .69:
            notes.append(["G",3])
        elif i < .78:
            notes.append(["G#",3])
        elif i < .81:
            notes.append(["A",3])
        elif i < .89:
            notes.append(["A#",3])
        elif i < 1:
            notes.append(["B",3])             
    count = 0
    for i in durations:
        notes[count].append(i)
        count+=1

        
    j = json.dumps(notes, indent = 2)
    print(j)
        
    



    
    






