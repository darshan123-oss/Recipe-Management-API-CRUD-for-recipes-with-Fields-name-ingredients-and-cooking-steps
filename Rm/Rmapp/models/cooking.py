from django.db import models
from ninja import Schema

class Cooking(models.Model):
    method = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.method


class CookingMethodInSchema(Schema):
    method: str
    description: str


class CookingMethodOutSchema(Schema):
    id: int
    method: str
    description: str


class CookingMethodListSchema(Schema):
    id: int
    method: str
