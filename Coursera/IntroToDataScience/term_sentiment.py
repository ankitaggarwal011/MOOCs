# -*- coding: utf-8 -*-
import sys
import urllib
import json

unlistdic={}
def hw(data,words):
    #print data
    score=0.0
    unlist=[]
    if data.get(u'text',0)!=0:
        for word in data[u'text'].split():
            if word in words.keys():
                score+=int(words[word])
            else:
                unlist.append(word)
    for i in range(len(unlist)):
        if unlist[i] in unlistdic.keys():
            unlistdic[unlist[i]].append(score)
        else:
            unlistdic[unlist[i]]=[score]
        

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    words = {}
    for line in sent_file:
        line = line.strip()
        parts = [p.strip() for p in line.split("\t")]
        words[unicode(parts[0], "UTF-8")] = parts[1]
    for t in tweet_file:
        data=json.loads(t)
        hw(data,words)
        #print score
    #print unlistdic
    for i in range(len(unlistdic.keys())):
        print "%s %.3f"%(unlistdic.keys()[i].encode('utf-8'),sum(unlistdic[unlistdic.keys()[i]]))
    sent_file.close()
    tweet_file.close()
    #lines(open(sys.argv[1]))
    #lines(open(sys.argv[2]))

if __name__ == '__main__':
    main()
