import math
import queue
import random
def binarySearch_helper(array,low,high,k):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if(array[mid] == k):
        return mid 
    if(array[mid] > k):
        return binarySearch_helper(array,low,mid-1,k)
    return binarySearch_helper(array,mid+1,high,k)

def binarySearch(arr,k):
    if(arr == []):
        return -1
    return binarySearch_helper(arr,0,len(arr),k)

def sieve(n):
    is_prime = [(i > 1) for i in range(n+1)]
    sqrt_n = int(math.sqrt(n))
    for i in range(sqrt_n+1):
        if(is_prime[i]):
            for j in range(i*i,n+1,i):
                is_prime[j] = False
    return is_prime

def bfs(graph):
    beenTraversed = [0 for _ in range(len(graph))]
    q = queue.Queue()
    count = 0
    for i in range(len(graph)):
        if(beenTraversed[i] == 0):
            q.put(i)
            while(not q.empty()):
                curNode = q.get()
                if(beenTraversed[curNode] == 0):
                    count += 1
                    beenTraversed[curNode] = count
                    for j in graph[curNode]:
                        if(beenTraversed[j] == 0):
                            q.put(j)
    return beenTraversed

def dfs_helper(graph,i,count,beenTraversed):
    count += 1
    beenTraversed[i] = count 
    for j in graph[i]:
        if(beenTraversed[j] == 0):
            count = dfs_helper(graph,j,count,beenTraversed)
    return count

def dfs(graph):
    beenTraversed = [0 for _ in range(len(graph))] 
    count = 0
    for i in range(len(graph)):
        if beenTraversed[i] == 0:
            count = dfs_helper(graph,i,count,beenTraversed)
    return beenTraversed

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def lomuto_partition(arr,low,high):
    piv = random.randint(low,high-1)
    swap(arr,piv,low)
    l = arr[low]
    s = low
    for i in range(low,high):
        if arr[i] < l:
            s += 1
            swap(arr,i,s)
    swap(arr,low,s)
    return s

def quickSort_helper(arr,low,high):
    if(low < high):
        s = lomuto_partition(arr,low,high)
        quickSort_helper(arr,low,s)
        quickSort_helper(arr,s+1,high)

def quickSort(arr):
    return quickSort_helper(arr,0,len(arr))

def mergeSort_helper(arr,scratch,low,high):
    if(low < high):
        mid = low + ((high-1)-low)//2
        mergeSort_helper(arr,scratch,low,mid)
        mergeSort_helper(arr,scratch,mid+1,high)
        L = low
        H = mid+1
        K = low
        for K in range(low,high):
            if L < mid and (H > high or arr[L] < arr[H]):
                scratch[K] = arr[L]
                L += 1
            else:
                scratch[K] = arr[H]
                H += 1
        for i in range(low,high):
            arr[i] = scratch[i]
def mergeSort(arr):
    scratch = [0 for _ in range(len(arr))]
    mergeSort_helper(arr,scratch,0,len(arr)-1)

graph = [[1,2,3],[0,4,5],[0,6,7],[0,7],[1],[1],[2],[2,3]]
graph2 = [[1,2],[0,2,3],[0,1,2],[1,2]]
graph3 = [[1,2,3],[0,4],[0,3],[0,2,4],[1,3]]
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sortableArr = [random.randint(0,100) for _ in range(10)]

print(list(map(lambda x: x[0],filter(lambda x: x[1], enumerate(sieve(4))))))
print(binarySearch(arr,15))
print(binarySearch([],0))
print(arr[binarySearch(arr,15)])
print(bfs(graph))
print(bfs(graph2))
print(bfs(graph3))
print(dfs(graph))
print(dfs(graph2))
print(dfs(graph3))
print(sortableArr)
quickSort(sortableArr)
print(sortableArr)
random.shuffle(sortableArr)
print(sortableArr)
mergeSort(sortableArr)
print(sortableArr)

