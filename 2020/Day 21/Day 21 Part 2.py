import re

#### PRE-COMPILE REGEXES FOR EFFICIENCY ####
a = re.compile(r'\(contains (.*)\)') # extracts only allergens
i = re.compile(r'(.*) \(')			 # extracts only ingredients

def stripAllergens(food: str) -> list:
	"""
	Extracts a list of allergens from a food's ingredients label

	Parameters:
	food - the label to extract the allergens from
	"""
	agens = re.search(a, food).groups()[0]
	return agens.split(', ')

def stripIngredients(food: str) -> list:
	"""
	Extracts the ingredient list from the food's ingredients label
	
	Parameters:
	food - the label to extract ingredients from
	"""
	ings = re.search(i, food).groups()[0]
	return ings.split(' ')

######################################################################################################

with open('input.txt', 'r') as file:
	foods = file.read().split('\n')

allergens = {} # maps an allergen to the foods that contain it
ingredients = {} # maps an ingredient to the foods that contain it
ingToAllergen = {} # maps an ingredient to the allergens it could possibly contain
allAllergens = set()
allIngredients = set()

# for each of the foods in the list...
for food in foods:
	# ... extract the allergens and ingredients contained...
	allers = stripAllergens(food)
	ingreds = stripIngredients(food)

	# ... compile a list of allergens, and a dictionary of which foods have the allergen...
	for allergen in allers:
		if allergen not in allergens.keys():
			allergens[allergen] = []

		allergens[allergen].append(food)
		allAllergens.add(allergen)

	# ... and compile a list of ingredients, which allergens *may* be present in
	# any of the given ingredients, and which foods contain the ingredient
	for ingredient in ingreds:
		allIngredients.add(ingredient)
		if ingredient not in ingToAllergen.keys():
			ingToAllergen[ingredient] = set()

		ingToAllergen[ingredient] |= set(allergens)

		if ingredient not in ingredients.keys():
			ingredients[ingredient] = []

		ingredients[ingredient].append(food)

# for each allergen...
for allergen in allAllergens:
	# ... look at all lists which contain it...
	presentIn = allergens[allergen]
	for food in presentIn:
		# ... and remove the allergen from any ingredients NOT in the food.
		presentIngredients = stripIngredients(food)
		excludedIngredients = allIngredients - set(presentIngredients)

		for ingredient in excludedIngredients:
			if allergen in ingToAllergen[ingredient]:
				ingToAllergen[ingredient].remove(allergen)

# split allergen free and dangerous ingreidents
allergenFreeIngredients = [ingred for ingred in allIngredients if len(ingToAllergen[ingred]) == 0]
dangerousIngredients = allIngredients - set(allergenFreeIngredients)

hazardList = {} # maps an allergen to the ingredient that has it

changeMade = True
while changeMade:
	changeMade = False
	# for each ingredient in the danger list...
	for ingredient in dangerousIngredients:
		# ... if the ingredient has exactly one allergen (aka it's guaranteed)...
		if len(ingToAllergen[ingredient]) == 1 and ingredient not in hazardList.keys():
			changeMade = True # allow another pass

			# ... associate the ingredient and allergen in the hazard list...
			hazardList[ingredient] = list(ingToAllergen[ingredient])[0]

			# ... then remove the allergen from all other ingredients
			for key in ingToAllergen.keys():
				if key == ingredient: continue # don't remove from the original ingredient

				if hazardList[ingredient] in ingToAllergen[key]:
					ingToAllergen[key].remove(hazardList[ingredient])

# finally, we need to sort the ingredients in alphabetical order by allergen
hazardsSorted = sorted(hazardList, key=lambda k: hazardList[k])

print("Resulting canonical list (remember not to include the ending comma!):")
for hazard in hazardsSorted:
	print(f'{hazard},', end='')