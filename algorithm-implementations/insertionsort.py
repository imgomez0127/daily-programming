import random
def insertionSort(lst):
	for i in range(1,len(lst)):
		nextPos = i
		heldItem = lst[nextPos]
		while(nextPos != 0 and lst[nextPos-1] > heldItem):
			lst[nextPos] = lst[nextPos-1]
			nextPos -= 1 
		lst[nextPos] = heldItem
	return lst
if __name__ == '__main__':
	arr = [1,5,3,2,4,10,55,12,11,1000,69,420]
	arr2 = [420,69,10,9,8,7,6,5,4,3,2,1]
	arr3 = []
	for i in range(1,10000):
		arr3.append(random.randint(0,5000))
	print(insertionSort(arr))
	print(insertionSort(arr2))
	print(insertionSort(arr3))