class Solution: 
    def longestPalindrome(self, s):
        cur_max = ""
        string_length = len(s)
        for i in range(string_length):
            for j in range(string_length):
                reversed_string = "".join(reversed(s[i:j]))
                if s[i:j] == reversed_string and len(reversed_string) > len(cur_max):
                    cur_max = s[i:j]
        return cur_max
                 
              
        
# Test program
s = "tracecars"
print(s)
print(str(Solution().longestPalindrome(s)))
# racecar
