"""
   Name    : leetcode1249.py
   Author  : Ian Gomez
   Date    : September 3, 2020
   Description :
   Github  : imgomez0127@github
"""
from queue import LifoQueue

class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = LifoQueue()
        buff = []
        for i,char in enumerate(s):
            if char == "(":
                stack.put(len(buff))
            elif char == ")":
                if stack.empty():
                    continue
                stack.get()
            buff.append(char)
        while not stack.empty():
            i = stack.get()
            buff = buff[:i]+buff[i+1:]
        return "".join(buff)

if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
    print(Solution().minRemoveToMakeValid("))(("))
    print(Solution().minRemoveToMakeValid("a)b(c)d"))
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
