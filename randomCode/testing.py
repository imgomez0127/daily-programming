def change(amt,Curr):
	if Curr == 0:
		return 0
	if amt == [] or Curr<0:
		return float("inf")
	if Curr - amt[0] < 0:
		return change(amt[1:],Curr)
	useit = 1 + change(amt,Curr-amt[0])
	loseit = change(amt[1:],Curr)
	return min(useit,loseit)
if __name__ == "__main__":
	print(change([1, 3, 16, 30, 50],35))