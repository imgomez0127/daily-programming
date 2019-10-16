def find_min_max(nums):
    min_val = min(nums[0],nums[1])
    max_val = max(nums[0],nums[1]) 
    for i in range(2,len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
        elif nums[i] > max_val:
            max_val = nums[i]
    return min_val,max_val
print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
