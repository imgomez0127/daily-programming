def max_subarray_sum(arr):
    max_val = max(arr)
    for window_size in range(len(arr)):
        for i in range(len(arr)):
            max_val = max(max_val,sum(arr[i:i+window_size+1]))
    return max_val

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137


