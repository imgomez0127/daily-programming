def subsetsum(arr):
	arr1 = sorted(arr)
	arr2 = set()
	cumsum = 0
	for i in range(len(arr1)):
		arr2.add(arr1[i])
		cumsum += arr[i]
		arr2.add(cumsum)
	smallestVal = 1
	flag = True
	print(arr2)
	for num in arr2:
		if(smallestVal < num):
			return smallestVal
		smallestVal += 1
	return smallestVal + 1
def subsetSum(arr):
	arr.sort()
	i = 0
	res = 1
	while(i < len(arr) and res >= arr[i]):
		res = res + arr[i]
		i += 1
	return res
if __name__ == '__main__':
	arr = [4,13,2,3,1]
	print(subsetsum(arr))
	print(subsetSum(arr))