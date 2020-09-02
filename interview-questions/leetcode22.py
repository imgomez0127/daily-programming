#Idea 1 generate all paren types and then filter for balanced parens (v slow)
from typing import List
class Solution:
    def __init__(self):
        self.ans = []
    def generateParenthesis_helper(self, l_amt, r_amt, S):
        if l_amt == 0 and r_amt == 0:
            self.ans.append(S)
            return
        if l_amt > 0:
            self.generateParenthesis_helper(l_amt-1, r_amt, S+"(")
        if r_amt > l_amt:
            self.generateParenthesis_helper(l_amt, r_amt-1, S+")")

    def generateParenthesis(self, n: int) -> List[str]:
        self.generateParenthesis_helper(n, n, "")
        return self.ans

print(Solution().generateParenthesis(3))
