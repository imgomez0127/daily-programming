import queue
class Solution:
    def get_bracket_index(self,bracket,brackets_list):
        for i,opening_bracket in enumerate(brackets_list):
            if bracket == opening_bracket:
                return i
        return -1 
    
    def is_corresponding_bracket(self,bracket1,bracket2):
        opening_brackets = ["[","(","{"]
        closing_brackets = ["]",")","}"]
        opening_bracket_index = self.get_bracket_index(bracket1,opening_brackets)
        return bracket2 == closing_brackets[opening_bracket_index]

    def isValid(self, s):
        opening_brackets = {"[","{","("}
        stack = queue.LifoQueue()
        for bracket in s:
            if bracket in opening_brackets:
                stack.put(bracket)
            else:
                top_bracket = stack.get()
                if not self.is_corresponding_bracket(top_bracket,bracket):
                    return False
        if not stack.empty():
            return False
        return True 
            
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "{[}]"
print(Solution().isValid(s))

