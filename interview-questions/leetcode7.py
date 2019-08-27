class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return_val = int("".join(reversed(str(x)))) 
            return 0 if return_val > 2 ** 31 - 1 else return_val 
        return_val = -int("".join(reversed(str(abs(x))))) 
        return 0 if return_val < -2 ** 31 else return_val
