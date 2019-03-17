def swap(L,i,j):
	temp = L[i]
	L[i] = L[j]
	L[j] = temp
def lomutopartition(L):
	l = L[0]
	s = 0
	for i in range(len(L)):
		if L[i] < l:
			s += 1
			swap(L,s,i)
	swap(L,0,s)
	return s
def quickSelect(L,k):
	s = lomutopartition(L)
	if s == k-1:
		return A[s]
	elif s > k -1:
		quickSelect(L[:s-1])
if __name__ == '__main__':
	L = [6,4,3,1,2,7,8,9]
	lomutopartition(L)
	print(L)
	lomutopartition(L)
	print(L)
