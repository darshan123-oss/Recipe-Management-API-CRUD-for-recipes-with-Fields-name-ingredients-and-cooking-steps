from django.db import models
from ninja import Schema


class Ingredient(models.Model):
    
    name = models.CharField(max_length=255)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=50, choices=[("g", "Grams"), ("ml", "Milliliters"), ("pcs", "Pieces")])

    def __str__(self):
        return self.name

class IngredientInSchema(Schema):
    name: str
    quantity: float
    unit: str

class IngredientOutSchema(Schema):
    id: int
    name: str
    quantity: float
    unit: str

class IngredientListSchema(Schema):
    id: int
    name: str
