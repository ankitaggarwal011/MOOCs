# -*- coding: utf-8 -*-
import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])
    words=[]
    for t in tweet_file:
        data=json.loads(t)
        if data.get(u'text',0)!=0:
            for word in data[u'text'].split():
                words.append(word.strip()) 
    fwords=dict(Counter(words))
    #total=1/len(fwords.keys())
    for i in range(len(fwords.keys())):
        #print fwords[fwords.keys()[i]]
        count=fwords.keys()[i]
        print "%s %.3f"%(count.encode('utf-8'),fwords[count])      
    tweet_file.close()

if __name__ == '__main__':
    main()
