from textblob import TextBlob
import json

import sys
import random

#print("number of arguments:", len(sys.argv), "arguments")
#print("argument list:", str(sys.argv))

class sentiment:

    def getSentiment(text):

        sentence_count = 0
        total_sent = 0

        blob = TextBlob(text)
        sentiment_list = []
        word_list = []
        word_count_list = []

        for sentence in blob.sentences:
            sent = round(sentence.sentiment.polarity, 3)
            total_sent += sent
            sentence_count += 1
            sentiment_list.append(sent)
            word_count = 0
            i = " "
            words = sentence.split(" ")
            for i in words:
                word_list.append(i)
                word_count += 1
            word_count_list.append(word_count)


        #for i in sentiment_list:



        final = [word_list, sentiment_list, word_count_list]

        return final

    with open("sent_test.txt", "r+") as f:
        fread = f.read()

    final = getSentiment(sys.argv[1])

    word_list = final[0]
    sentiment_list = final[1]
    word_count_list = final[2]


    '''
    durations = []
    for i in words:
        duration = 1.6 / i
        durations.append(duration)
    #print(durations)
    '''


    notes = []

    with open("sent_test.txt", "r+") as f:
        text = f.read()
    blob = TextBlob(text)

    words_list = []

    sentiment_list = []
    for sentence in blob.sentences:
        sent = round(sentence.sentiment.polarity, 3)
        sentiment_list.append(sent)
        words = sentence.split(" ")
        for word in words:
            words_list.append(word)


    def pitchOctave(sent):
        #declare arrays

        c_mjr = ["C","D","E","F","G","A","B"]                     #middle
        g_mjr = ["G", "A", "B", "C", "D", "E", "F#"]   #slight happy
        d_minor = ["D", "E", "F", "G", "A", "A#", "C"]        #slight sad
        d_mjr = ["D", "E", "F#", "G", "A", "B","C#"]         #super happy
        g_minor = ["G", "A", "A#", "C", "D", "D#","F"]           #super sad

        octave = 3
        rn = random.randint(0,6)

        if sent < .4 and sent >= -.4:
            pitch = c_mjr[rn]            # if in middle, retun a not in c major, create an array
        elif sent > .4 and sent < .6:     # if more positive
            pitch = g_mjr[rn]           # a little more happy
            octave += 1
        elif sent < -.4 and sent >-.6:  # if more negative
            pitch = d_minor[rn]         # a little more sad
            octave -=1
        elif sent > .6:                #fuck im happy
            pitch = d_mjr[rn]
            octave += 2
        elif sent > -.6:                 # worst
            pitch = g_minor[rn]
            octave -= 2

        result = [pitch, octave]

        return result

    note_octave = []
    for sentiment in sentiment_list:
        note_octave.append(pitchOctave(sentiment))
    """
    count = 0
    for i in durations:
        note_octave[count].append(i)
        count += 1
    """
    count = 0
##
##    words = []
##    for i in this:
##        words.append(i[0])
##
##    for i in words:
##        note_octave[count].append(i)
##        count += 1


    curCount = 0
    curSent = 0
    for i in word_count_list:
        sentence = ""
        for k in range(0, i):
            sentence += word_list[curCount] + " "
            curCount += 1
        note_octave[curSent].append(sentence)
        curSent += 1

    print(note_octave)
