"""
    leetcode version of this problem
"""
def swap(lst,a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
def fun(lst,k):
    if(k == 0):
        return lst
    if(len(lst) % k == 0):
        for i in range(len(lst)-1,0+k,-1):
            newIndex = (i + k) % len(lst)
            swap(lst,newIndex,i) 
    else:
        oldVal = lst[0]
        oldIndex = 0
        for _ in range(len(lst)-1,0+k,-1): 
            newIndex = (oldIndex +k) % len(lst)
            temp = lst[newIndex]
            lst[newIndex] = oldVal
            oldVal = temp
            oldIndex = newIndex     
    return lst
if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    print(fun(lst,3))

