# Dictionary Methods

recipe = {
    "recipeName": "Musakka",
    "recipeDescription": "recipe description",
    "image": "1.jpg"
}

# Access items
result = recipe["recipeName"]
result = recipe.get("recipeName")
result = recipe.keys()
result = recipe.values()
result = recipe.items()

# Update items
# recipe["recipeName"] = "Mantı"
# recipe.update({"recipeName": "Mantı"})
# recipe.update({"recipeName2": "Mantı"})

# Delete items
# recipe.pop("recipeName")
# recipe.popitem()
recipe.clear()

# Copy => reference

result = recipe

print(result)

# Output:

"""

{}

"""