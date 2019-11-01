
def BinaryReflectedGrayCodes(n):
    if n == 1:
        return [[0],[1]]
    lst1 = BinaryReflectedGrayCodes(n-1)
    lst2 = list(reversed(lst1))
    for i in range(len(lst1)):
        lst1[i] = [0] + lst1[i]
        lst2[i] = [1] + lst2[i]
    lst1.extend(lst2)
    return lst1

print(BinaryReflectedGrayCodes(4))
