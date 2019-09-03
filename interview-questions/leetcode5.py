import string
class Solution:
    def find_new_starting_char(self,s,c):
        for i,char in enumerate(s):
            if char == c:
                return i+1
        return -1
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_len = 1
        starting_char = 0
        seen_chars = {char: -1 for char in string.printable}
        seen_chars[s[0]] = 0
        for i in range(1,len(s)):
            if seen_chars[s[i]] != -1:
                starting_char = max(starting_char,min(seen_chars[s[i]] + 1,len(s)-1))
            print(starting_char)
            max_len = max(max_len,i-starting_char+1)
            seen_chars[s[i]] = i
        return max_len

print(Solution().lengthOfLongestSubstring("abba"))
