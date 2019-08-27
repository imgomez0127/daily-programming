class Solution:
    def __init__(self):
        self.cache = {}
    def minDistance(self, word1: str, word2: str) -> int:
        if (word1,word2) in self.cache:
            return self.cache[(word1,word2)]
        else:
            if word1 == "":
                return len(word2)
            if word2 == "":
                return len(word1)
            if word1[0] == word2[0]:
                return self.minDistance(word1[1:],word2[1:])
            insertion = self.minDistance(word1[1:],word2) + 1
            deletion = self.minDistance(word1,word2[1:]) + 1
            replacement = self.minDistance(word1[1:],word2[1:]) + 1
            answer = min(insertion,deletion,replacement)
            self.cache[(word1,word2)] = answer
            return answer
if __name__ == "__main__":
    print(Solution().minDistance('biting', 'sitting'))
    print(Solution().minDistance("hello", "hello"))
    print(Solution().minDistance("helllo","hello"))

