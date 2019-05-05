"""
    This question was asked by triplebyte[medium]
    Given a list of numbers e.g [1,2,3,4]
    and a list of probabilities for a respective number
    [0.1,0.5,0.2,0.2] create a function to model the probability
""" 
from random import random
def fun(numsLst,probsLst):
    generatedNumber = random()
    probabilityThreshold = 0
    for i,probability in enumerate(probsLst):
        probabilityThreshold += probability
        if generatedNumber < curSum:
            return numsLst[i] 

if __name__ == "__main__":
    sumOfNums = [0 for _ in range(8)]
    iterations = 100000
    for _ in range(iterations):
        sumOfNums[fun([1,2,3,4,5,6,7,8],[0.1,0.2,0.1,0.2,0.05,.3,.025,.025])-1]+=1
    print(list(map(lambda x: x/iterations,sumOfNums)))
