"""
    Asked by Microsoft find the length of longest consecutive elements sequence
"""
def fun1(lst):
    maxElement = max(lst)
    sequence = [False for _ in range(maxElement)]
    for n in lst:
        sequence[n-1] = True
    largestSequence = 0
    curSequence = 0
    for i in range(len(sequence)):
        if(sequence[i] == False):
            largestSequence = max(curSequence,largestSequence)
            curSequence = 0
            continue
        curSequence += 1
    return max(largestSequence,curSequence)
if __name__ == "__main__":
    print(fun1([100,4,200,1,3,2]))
