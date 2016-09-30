# -*- coding: utf-8 -*-
import sys
import urllib
import json


def hw(data,words):
    #print data
    score=0.0
    if data.get(u'text',0)!=0:
        for word in data[u'text'].split():
            if word in words.keys():
                score+=int(words[word])
        #print score
    if ("place" in data and data["place"] is not None and "full_name" in data["place"] and data["place"]["full_name"] is not None and "country_code" in data["place"] and data["place"]["country_code"] is not None):
        if data["place"]["country_code"]=="US":
            return [data["place"]["full_name"][-2:],score]
        else:
            return [0,0]
    else:
        return [0,0]

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    words = {}
    hscore=0.0
    for line in sent_file:
        line = line.strip()
        parts = [p.strip() for p in line.split("\t")]
        words[unicode(parts[0], "UTF-8")] = parts[1]
    for t in tweet_file:
        data=json.loads(t)
        [state,score]=hw(data,words)
        if score>hscore:
            hstate=state
            hscore=score
        else:
            hstate="NA"
            hscore=0
    print hstate
    sent_file.close()
    tweet_file.close()
    #lines(open(sys.argv[1]))
    #lines(open(sys.argv[2]))

if __name__ == '__main__':
    main()
