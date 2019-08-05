def sortNums(nums):
    num_set = set(nums)
    list1 = [num_set.pop()]
    list2 = [num_set.pop()]
    list3 = [num_set.pop()]
    for num in nums:
        if num == list1[0]:
            list1.append(num)
        if num == list2[0]:
            list2.append(num)
        if num == list3[0]:
            list3.append(num)
    list1.pop()
    list2.pop()
    list3.pop()
    return list1 + list2 + list3
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
#TODO const space implementation
