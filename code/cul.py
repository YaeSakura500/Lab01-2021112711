import re
import networkx as nx
import numpy as np
import random

from pyparsing import Word


class cul(object):
    def __init__(self, G, Adj_Mat, word2node, node2word):
        super(cul, self).__init__()
        self.G = G
        self.M = Adj_Mat
        self.w2n = word2node
        self.n2m = node2word

    # find brdge word list,suppose that word1 and word2 are in the node list
    def queryBridgeWordList(self, word1: str, word2: str):
        wordlist=[]
        node1 = self.w2n[word1]
        node2 = self.w2n[word2]
        for i in range(len(self.w2n)):
            if self.M[node1][i]!=0 and self.M[i][node2]!=0:
                wordlist.append(self.n2m[i])
        return wordlist

    # String queryBridgeWords(String word1, String word2)：查询桥接词
    def queryBridgeWords(self, word1: str, word2: str):
        '''
        :param word1:
        :param word2:
        :return:
        '''
        # turn query words into lower case
        Word1 = word1.lower()
        Word2 = word2.lower()
        # Case:Not in the node list 
        if Word1 not in self.w2n or Word2 not in self.w2n:
            return f'No "{word1}" or "{word2}" in the graph!'
        # init bridge word list
        wordlist = self.queryBridgeWordList(Word1,Word2)
        #Case:no bridge word
        if len(wordlist)==0:
            return f'No bridge words from "{word1}" to "{word2}"!'
        #Cases:got bridge word
        elif len(wordlist)==1:
            return f'The bridge words from "{word1}" to "{word2}" is:{wordlist[0]}.'
        else:
            return f'The bridge words from "{word1}" to "{word2}" are:' + ' ,'.join(wordlist[:-1]) + f'and {wordlist[-1]}.'
    # String generateNewText(String inputText)：根据bridge word生成新文本

    def generateNewText(self, inputText: str):
        # In order to handel any possible cases, we use Try...except...finally structure
        try:
            # get all the word pair and find bridge word.if found add it into finally output
            words = inputText.lower().split()
            Words = inputText.split()
            out = ''
            i = 0
            # find the first word in our nodes
            while words[i] not in self.w2n:
                out += Words[i]
                out += ' '
                i += 1
            # find last words
            out += Words[i]
            out += ' '
            i += 1
            last =1
            while i in range(len(words)):
                if words[i] in self.w2n and last == 1:
                    wordlist = self.queryBridgeWordList(words[i-1],words[i])
                    if wordlist != []:
                        out += random.choice(wordlist)
                        out += ' '
                elif words[i] in self.w2n and last == 0:
                    last = 1
                elif words[i] not in self.w2n:
                    last = 0
                out += Words[i]
                out += ' '
                i += 1
            return out[:-1]
        except:
            pass
        finally:
            return out

    # String calcShortestPath(String word1, String word2)：计算两个单词之间的最短路径
    def calcShortestPath(self, word1: str, word2: str):
        pass

    # String randomWalk()：随机游走
    def randomWalk(self):
        pass