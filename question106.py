"""
    Question was asked by pinterest
"""
def fun(lst):
    if(lst == []):
        return False
    if(lst[0] == 0):
        return False
    if(lst[0] >= len(lst)-1):
        return True
    canGetOut = False
    for i in range(1,lst[0]+1):
        canGetOut = canGetOut or fun(lst[i:]) 
    return canGetOut
if __name__ == "__main__":
    print(fun([2,0,1,0]))
    print(fun([1,1,0,1]))
