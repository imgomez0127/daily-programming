def f(C):
    F = [[0 for _ in range(len(C[0]))] for _ in range(len(C))]
    F[len(C)-1][len(C[0])-1] = C[len(C)-1][len(C[0])-1]
    for col in range(len(C[0])-2,-1,-1):
        F[len(C)-1][col] = C[len(C)-1][col] + F[len(C)-1][col+1]
    for row in range(len(C)-2,-1,-1):
        F[row][len(C[0])-1] = C[row][len(C[0])-1] + F[row+1][len(C[0])-1]
    row = 0
    col = 0
    for row in range(len(C)-2,-1,-1):
        for col in range(len(C[0])-2,-1,-1):
                F[row][col] = C[row][col] + max(F[row][col+1],F[row+1][col])
    return F

print(f([[1,0,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,0],[1,0,0,1]]))
