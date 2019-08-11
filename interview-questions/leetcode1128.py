class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        existing_pairs = {}
        amount = 0
        for domino in dominoes:
            if tuple(domino) in existing_pairs:
                existing_pairs[tuple(domino)] += 1
                amount += existing_pairs[tuple(domino)]
            elif tuple(reversed(domino)) in existing_pairs:
                existing_pairs[tuple(reversed(domino))] += 1
                amount += existing_pairs[tuple(reversed(domino))]
            else:
                existing_pairs[tuple(domino)] = 0 
        return amount

if __name__ == "__main__":
    #Ans should be 1
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    #Ans should be 0
    dominoes2 = []
    #Ans should be 1
    dominoes3 = [[3,4],[3,4],[4,5],[6,7]]
    #Ans should be 0
    dominoes4 = [[1,2],[3,4],[5,6],[7,8]]
    #Ans should be 6
    dominoes5 = [[1,2],[2,1],[1,2],[2,1]]
    print(Solution().numEquivDominoPairs(dominoes))
    print(Solution().numEquivDominoPairs(dominoes2))
    print(Solution().numEquivDominoPairs(dominoes3))
    print(Solution().numEquivDominoPairs(dominoes4))
    print(Solution().numEquivDominoPairs(dominoes5))
