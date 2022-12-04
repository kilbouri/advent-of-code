from os.path import dirname
import re

a = re.compile(r"\(contains (.*)\)")  # extracts only allergens
i = re.compile(r"(.*) \(")			  # extracts only ingredients


def stripAllergens(food: str) -> list:
    agens = re.search(a, food).groups()[0]
    return agens.split(", ")


def stripIngredients(food: str) -> list:
    ings = re.search(i, food).groups()[0]
    return ings.split(" ")


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        foods = file.read().split("\n")

    allergens = {}  # maps an allergen to the foods that contain it
    ingredients = {}  # maps an ingredient to the foods that contain it
    ingToAllergen = {}  # maps an ingredient to the allergens it could possibly contain
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
    allergenFreeIngredients = [
        ingred for ingred in allIngredients if len(ingToAllergen[ingred]) == 0]
    occurenceCount = 0
    for ingredient in allergenFreeIngredients:
        occurenceCount += len(ingredients[ingredient])

    print(f"There are {occurenceCount} occurences of"
          + " ingredients which do not have any allergens.")


if __name__ == "__main__":
    main()
