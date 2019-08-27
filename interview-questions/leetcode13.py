class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_value = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        value = 0
        for i,char in enumerate(s):
            value += char_value[char] 
            if i != 0 and char_value[s[i-1]] < char_value[char]:
                value -= char_value[s[i-1]] * 2
        return value
