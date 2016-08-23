# -*- coding: utf-8 -*-

import sys

def main():
    word2freq = {}
    entity2freq = {}
    label2freq = {}
    with open(sys.argv[1]) as f:
        for line in f:
            temp = line.strip().split("\t")
            labels, entity, words = temp[2],temp[1],temp[-1]
            for label in labels.split():
                if label not in label2freq:
                    label2freq[label] = 1
                else:
                    label2freq[label] += 1
            for word in words.split():
                if word not in word2freq:
                    word2freq[word] = 1
                else:
                    word2freq[word] += 1
            if entity not in entity2freq:
                entity2freq[entity] = 1
            else:
                entity2freq[entity] += 1

    def _local(file_path, X2freq):
        with open(file_path,"w") as f:
            for i,(X,freq) in enumerate(sorted(X2freq.items(),key = lambda t: -t[1])):
                f.write(str(i)+"\t"+X+"\t"+str(freq)+"\n")

    _local(sys.argv[2],word2freq)
    _local(sys.argv[3],entity2freq)
    _local(sys.argv[4],label2freq)
    
if(__name__=='__main__'):
    main()
