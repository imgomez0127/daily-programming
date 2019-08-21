class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_set = set(J)
        return sum(map(lambda x: x in jewel_set,list(S)))
