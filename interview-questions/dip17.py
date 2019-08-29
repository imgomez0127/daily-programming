def maximum_product_of_three(lst):
    max_product = float("-inf")
    for i in range(len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                max_product = max(max_product,lst[i]*lst[j]*lst[k])
    return max_product 

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
