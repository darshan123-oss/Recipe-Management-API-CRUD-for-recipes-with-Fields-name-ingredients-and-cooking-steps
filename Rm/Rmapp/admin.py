from django.contrib import admin
from Rmapp.models.cooking import Cooking
from Rmapp.models.ingredients import Ingredient
from Rmapp.models.recipe import Recipe

admin.site.register(Cooking)
admin.site.register(Ingredient)
admin.site.register(Recipe)
