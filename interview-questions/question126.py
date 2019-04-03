"""
    This question was asked by Facebook
"""
def swap(lst,a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
def fun(lst,k):
    for i in range(len(lst))):
        newIndex = (i - k) % len(lst)
        position =   
    return lst
if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8]
    print(fun(lst,3))
