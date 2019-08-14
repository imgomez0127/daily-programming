def f(lst):
  for i in range(len(lst)):
    dcopy = {}
    for num in lst:
      dcopy[num] = dcopy.get(num,0) + 1
    dcopy[lst[i]] -= 1
    for j in range(i,len(lst)):
      dcopy[lst[j]]-= 1
      last_triple = ((lst[i])**2 + (lst[j])**2)**0.5
      if dcopy.get(last_triple,0) > 0:
        return True
  return False
print(f([3,4,5]))
print(f([3,5,12,13]))
print(f([1,1,1]))
print(f([10,4,6,12,5]))
