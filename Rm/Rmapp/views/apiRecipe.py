from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from Rmapp.models.recipe import Recipe, RecipeInSchema, RecipeOutSchema, RecipeListSchema
from Rmapp.models.ingredients import Ingredient

rerouter = Router()

@rerouter.post("/recipe/", response={201: RecipeOutSchema})
def create_recipe(request, data: RecipeInSchema):
    ingredients = Ingredient.objects.filter(id__in=data.ingredients)
    new_recipe = Recipe.objects.create(
        title=data.title,
        description=data.description,
        instructions=data.instructions,
    )
    new_recipe.ingredients.set(ingredients)
    return new_recipe


@rerouter.get("/recipe/{recipe_id}/", response=RecipeOutSchema)
def get_recipe(request, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return RecipeOutSchema.from_orm(recipe)


@rerouter.get("/recipes/", response=List[RecipeListSchema])
def list_recipes(request):
    return Recipe.objects.all()
