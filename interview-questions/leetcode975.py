class Solution:
    def ableToJumpSomewhere(self,A,position,jump_number):
        if position == len(A)-1:
            return position
        if jump_number % 2 == 0:
            next_index = (float("-inf"),-1)
            for i in range(position+1,len(A)):
                if A[position] >= A[i]:
                    if A[i] > next_index[0]:
                        next_index = (A[i],i)
        else:
            next_index = (float("inf"),-1)
            
            for i in range(position+1,len(A)):
                if A[position] <= A[i]:
                    if A[i] < next_index[0]:
                        next_index = (A[i],i)
        return next_index[1]
    
    def oddEvenJumps(self, A):
        cache = {(len(A)-1,0):True,(len(A)-1,1):True}
        good_indices = 1
        for i in range(len(A)-2,-1,-1):
            position = i
            jump_number = 0
            visited_positions = []
            while(position != len(A)-1 and position != -1):
                jump_number += 1
                visited_positions.append((position,jump_number%2))
                if (position,jump_number%2) in cache:
                    if cache[(position,jump_number%2)]:
                        position = len(A)-1
                    else:
                        position = -1
                    break
                position = self.ableToJumpSomewhere(A,position,jump_number)
            visited_positions.append((position,jump_number%2))
            for visited_position in visited_positions:
                cache[visited_position] = position == (len(A)-1)
            if position == (len(A)-1):
                good_indices += 1
        return good_indices
                                                
print(Solution().oddEvenJumps([10,13,12,14,15]))

