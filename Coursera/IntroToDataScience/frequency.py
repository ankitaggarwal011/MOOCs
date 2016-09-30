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
    fwords=Counter(words)
    for letter, count in fwords.most_common(len(list(fwords))):
        print '%s %.3f' % (letter.encode('utf-8'), count)
    tweet_file.close()

if __name__ == '__main__':
    main()
