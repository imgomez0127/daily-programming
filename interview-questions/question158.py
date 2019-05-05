"""
    This question was asked by slack[medium]
"""
def fun(matrix,width,height):
    def fun_helper(i,j):
        if(i >= height):
            return 0
        if(j >= width):
            return 0
        if(i == height-1 and j == width-1):
            return 1
        if(matrix[i][j] == 1):
            return 0
        return fun_helper(i,j+1) + fun_helper(i+1,j)
    return fun_helper(0,0)
if __name__ == "__main__":
    matrix = [[0,0,1],[0,0,1],[1,0,0]]
    print(fun(matrix,len(matrix),len(matrix[0])))
    
