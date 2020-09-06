#!/usr/bin/env python3
from typing import List
from collections import Counter
from queue import Queue

class Solution:
    def __init__(self):
        self.q = Queue()
        self.seen = set()
        self.count = 0

    def compute_letter_diff(self, word1, word2):
        count = 0
        for char1, char2 in zip(word1,word2):
            count += char1 != char2
        return count

    def ladderLength_helper(self, endWord, wordList):
        while not self.q.empty():
            cur, count = self.q.get()
            print(cur, count)
            if cur == endWord:
                return count
            if cur not in self.seen:
                self.seen.add(cur)
                for word in wordList:
                    if word not in self.seen:
                        if self.compute_letter_diff(cur, word) == 1:
                            self.q.put((word,count+1))
        return 0


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.q.put((beginWord,1))
        return self.ladderLength_helper(endWord, wordList)

if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
