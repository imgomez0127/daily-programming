def fun(lst):
    if(lst == []):
        return -1
    def fun_helper(lst,low,high):
        if(low > high): 
            return -1
        mid = (high+low)//2
        if(lst[mid] != 0):
            if(mid == 0):
                return 0
            if(lst[mid-1] == 0):
                return mid
            return fun_helper(lst,low,mid-1)
        return fun_helper(lst,mid+1,high)
    return fun_helper(lst,0,len(lst)) 
if __name__ == "__main__":
    print(fun([]))
