from ninja import NinjaAPI
from Rmapp.views.apiRecipe import rerouter
from Rmapp.views.apiIngredient import irouter
from Rmapp.views.apiCooking import crouter

api = NinjaAPI()

api.add_router("/recipe/", rerouter)
api.add_router("/ingredient/", irouter)
api.add_router("/cooking/", crouter)
