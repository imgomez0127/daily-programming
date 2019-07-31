class Solution:
    def lengthOfLongestSubstring(self, s):
        if(s == ""):
            return 0
        start = 0
        max_length = 0
        seen = {}
        for i,char in enumerate(s):
            if char in seen:
                start = max(start,seen[char]+1)
            seen[char] = i
            max_length = max(max_length,i-start+1)
        return max_length
        

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
