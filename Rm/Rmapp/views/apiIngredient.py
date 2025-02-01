from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from Rmapp.models.ingredients import Ingredient, IngredientInSchema, IngredientOutSchema, IngredientListSchema

irouter = Router()

@irouter.post("/ingredient/", response={201: IngredientOutSchema})
def create_ingredient(request, data: IngredientInSchema):
    ingredient = Ingredient.objects.create(**data.dict())
    return ingredient

@irouter.get("/ingredient/{ingredient_id}/", response=IngredientOutSchema)
def get_ingredient(request, ingredient_id: int):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    return ingredient

@irouter.get("/ingredients/", response=List[IngredientListSchema]) 
def list_ingredients(request):
    return Ingredient.objects.all()
