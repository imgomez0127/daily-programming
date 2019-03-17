def knapsack(weight,items):
	if weight == 0:
		return 0
	if len(items) == 0:
		return 0
	if weight - items[0][0] < 0:
		return knapsack(weight,items[1:])
	grabCur = items[0][1] + knapsack(weight-items[0][0],items[1:])
	ditchCur = knapsack(weight,items[1:])
	if grabCur< ditchCur:
		return ditchCur
	return grabCur
print(knapsack(50,[(10,60),(20,100),(30,120)]))