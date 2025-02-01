from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from Rmapp.models.cooking import Cooking, CookingMethodInSchema, CookingMethodOutSchema, CookingMethodListSchema

crouter = Router()

@crouter.post("/cooking-method/", response={201: CookingMethodOutSchema})
def create_cooking_method(request, data: CookingMethodInSchema):
    method = Cooking.objects.create(**data.dict())
    return method

@crouter.get("/cooking-method/{method_id}/", response=CookingMethodOutSchema)
def get_cooking_method(request, method_id: int):
    method = get_object_or_404(Cooking, id=method_id)
    return method

@crouter.get("/cooking-methods/", response=List[CookingMethodListSchema]) 
def list_cooking_methods(request):
    return Cooking.objects.all()
