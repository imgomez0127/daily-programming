import random
def uber(arr):
	product = 1
	hasZero = False
	for item in arr:
		if item == 0:
			hasZero = True
			continue
		product *= item
	for i in range(len(arr)):
		if(hasZero and arr[i] == 0):
			arr[i] = product
		elif(hasZero):
			arr[i] = 0
		else:
			arr[i] = product// arr[i]
	return arr

if __name__ == '__main__':
	print(uber([1, 2, 3, 4, 5]))
	print(uber([3, 2, 1]))
	print(uber([0,1,2,3,4,5]))
	arr = [random.randint(1,10) for _ in range(100)]
	print(uber(arr))