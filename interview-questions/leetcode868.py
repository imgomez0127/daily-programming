class Solution:
    def binaryGap(self, N: int) -> int:
        binary_respresentation = str(bin(N))[2:]
        distances = []
        cur_distance = 0
        for i in range(len(binary_respresentation)):
            if binary_respresentation[i] == '1':
                break
        else:
            return 0
        for j in range(i,len(binary_respresentation)):
            if binary_respresentation[j] == '1':
                distances.append(cur_distance)
                cur_distance = 0
            cur_distance += 1 
        return max(distances) 
if __name__ == "__main__":
    num1 = 22
    num2 = 5
    num3 = 6
    num4 = 8
    num5 = 0
    print(Solution().binaryGap(num1))
    print(Solution().binaryGap(num2))
    print(Solution().binaryGap(num3))
    print(Solution().binaryGap(num4))
    print(Solution().binaryGap(num5))
