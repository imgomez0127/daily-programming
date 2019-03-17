def Google1(arr,k):
	itemSet = set()
	for item in arr:
		if k - item in itemSet:
			return True
		itemSet.add(item)
	return False
if __name__ == '__main__':
	print(Google1([10,15,3,7],17))
