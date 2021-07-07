#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	recipe_vals = list(recipe.values())
	ingredients_vals = list(ingredients.values())

	if len(ingredients_vals) < len(recipe_vals):
		return 0

	batches = []

	for i in range(0, len(recipe_vals)):
		batch = math.floor(ingredients_vals[i] / recipe_vals[i])
		batches.append(batch)

	min_batches = 0

	for i in range(1, len(batches) - 1):
		if batches[i] < batches[min_batches]:
			print(batches[i])
			print(batches[min_batches])
			min_batches = i
			print(min_batches)

	return batches[min_batches]


if __name__ == '__main__':
	# Change the entries of these dictionaries to test 
	# your implementation with different inputs
	recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
	ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))