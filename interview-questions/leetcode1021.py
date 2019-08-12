class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        def removeOuterParentheses_helper(S,available_parens):
            if S == "":
                return ""
            if S[0] == ")" and available_parens == 1:
                return removeOuterParentheses_helper(S[1:],0)
            if S[0] == "(" and available_parens == 0:
                return removeOuterParentheses_helper(S[1:],1)
            if S[0] == "(":
                return S[0] + removeOuterParentheses_helper(S[1:],available_parens+1)
            return S[0] + removeOuterParentheses_helper(S[1:],available_parens-1)
        return removeOuterParentheses_helper(S,0)
    
if __name__ == "__main__":
    s = "()()"
    s2 = "(()())(())"
    print(Solution().removeOuterParentheses(s))
    print(Solution().removeOuterParentheses(s2))
