class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if tree == []:
            return 0
        total_fruit_counts = []
        sequence_count = [1,0]
        fruit_count = [1,0]
        pointer1 = tree[0]
        pointer2 = -1
        for i in range(1,len(tree)):
            if tree[i] == tree[pointer1]:
                sequence_count[0] += 1
                fruit_count[0] += 1
                sequence_count[1] = 0
            elif tree[i] == tree[pointer2]:
                sequence_count[1] += 1
                fruit_count[1] += 1
                sequence_count[0] = 0
            else:
                #update the less of the pointer
                if pointer1 > pointer2:
                    pointer2 = fruit
                    sequence_count
            
