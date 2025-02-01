import datetime
from django.db import models
from ninja import Schema
from typing import List

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField("Rmapp.Ingredient", related_name="recipes")
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecipeInSchema(Schema):
    title: str
    description: str
    ingredients: List[int]  # List of ingredient IDs
    instructions: str


class IngredientBriefSchema(Schema):
    id: int
    name: str


class RecipeOutSchema(Schema):
    id: int
    title: str
    description: str
    ingredients: List[IngredientBriefSchema]
    instructions: str
    

class RecipeListSchema(Schema):
    id: int
    title: str
    description: str
