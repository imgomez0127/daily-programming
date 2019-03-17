from random import shuffle,randint

def sorted(array):
	for i in range(len(array)-1):
		if(array[i] > array[i+1]):
			return False
	return True
def bogosort(array):
	while(not sorted(array)):
		print(array)
		shuffle(array)
	return array
if __name__ == '__main__':
	arr = [randint(1,1000) for _ in range(11)]
	print(arr)
	bogosort(arr)
	print(arr)
