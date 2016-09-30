# -*- coding: utf-8 -*-
import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])
    words=[]
    for t in tweet_file:
        data=json.loads(t)
        if "entities" in data and "hashtags" in data["entities"] and data["entities"]["hashtags"]!=[]:
            for i in range(len(data["entities"]["hashtags"])):
                words.append(data["entities"]["hashtags"][i]["text"]) 
    fwords=Counter(words)
    #print fwords
    for letter, count in fwords.most_common(10):
        print '%s %.3f' % (letter.encode('utf-8'), count)
    tweet_file.close()

if __name__ == '__main__':
    main()
