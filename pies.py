pies_recipe={
	'Apple':[0,1,4,3,2],
	'Pumpkin':[1,0,3,4,3]
}
def bake_pies(ingredients):
	bakeableApple = []
	bakeablePumpkin = []
	for i in range(len(ingredients)):
		if(pies_recipe['Apple'][i] != 0):
			bakeableApple.append(ingredients[i]//pies_recipe['Apple'][i])
		if(pies_recipe['Pumpkin'][i] != 0):
			bakeablePumpkin.append(ingredients[i]//pies_recipe['Pumpkin'][i])

	minPumpkin = bakeablePumpkin[0]
	minApple = bakeableApple[0]
	for i in range(len(bakeableApple)):
		minApple = min(bakeableApple[i],minApple)
		minPumpkin = min(bakeablePumpkin[i],minPumpkin)
	if(minPumpkin == 0 and minApple == 0):
		return None
	elif(minPumpkin >= minApple):
		return 'Pumpkin'
	else:
		return 'Apple'
def max_pies(ingredients):
	cur_ingredients = ingredients
	curr_pie = bake_pies(cur_ingredients)
	pie_count = {
		'Pumpkin':0,
		'Apple':0,
	}
	print(curr_pie)
	while(curr_pie != None):
		print(curr_pie)
		pie_count[curr_pie] += 1
		for i in range(len(cur_ingredients)):
			cur_ingredients[i] -= pies_recipe[curr_pie][i]
		curr_pie = bake_pies(cur_ingredients)
		
	return pie_count
print(max_pies([12,14,20,42,24]))