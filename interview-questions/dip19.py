def max_subarray_sum(arr):
    max_sum = cur_sum = 0
    for num in arr:
        if num > cur_sum+num:
            max_sum = max(cur_sum,max_sum)
            cur_sum = num
        else:
            cur_sum += num
    return max(max_sum,cur_sum)

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137


