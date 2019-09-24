class Solution:
    def reverseWords(self,str):
        return " ".join(map(lambda x: x[::-1],str.split(" ")))

print(Solution().reverseWords("The cat in the hat"))
