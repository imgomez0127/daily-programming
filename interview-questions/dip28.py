def max_change_helper(mat,i,j):
    if i == len(mat)-1 and j == len(mat[0])-1:
        return mat[i][j]
    if i == len(mat)-1:
        return mat[i][j] + max_change_helper(mat,i,j+1)
    if j == len(mat[0])-1:
        return mat[i][j] + max_change_helper(mat,i+1,j)
    return mat[i][j] + max(max_change_helper(mat,i,j+1),max_change_helper(mat,i+1,j))

def max_change(mat):
    return max_change_helper(mat,0,0)
mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13
