"""
    This question was asked by triplebyte[medium]
    Given a list of numbers e.g [1,2,3,4]
    and a list of probabilities for a respective number
    [0.1,0.5,0.2,0.2] create a function to model the probability
""" 
from random import random
def fun(numsLst,probsLst):
    determiningNumber = random()
    curSum = 0
    for i,probability in enumerate(probsLst):
        curSum += probability
        if determiningNumber < curSum:
            return numsLst[i] 

if __name__ == "__main__":
    sumOfNums = [0 for _ in range(4)]
    iterations = 100000
    for _ in range(iterations):
        sumOfNums[fun([1,2,3,4],[0.1,0.5,0.2,0.2])-1]+=1
    print(list(map(lambda x: x/iterations,sumOfNums)))
