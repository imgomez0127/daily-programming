def subset_sum(vals,b):
    table = [[j == 0 for j in range(b+1)] for _ in range(len(vals)+1)]
    for i in range(1,len(table)):
        for j in range(1,len(table[i])):
            table[i][j] = ((table[i-1][j]) or
                           ((vals[i-1] <= j) and (table[i-1][j-vals[i-1]])))
    list1 = []
    for row in table:
        print(row)
    while i!= 0 and j!=0:
      if(not table[i-1][j]):
        list1.append(vals[i-1])
        j-=vals[i-1]
        i-=1
      else:
        i-=1
    print(list(reversed(list1)))
