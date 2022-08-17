from django.contrib import admin
from .models import MenuItem, Ingredients, RecipeRequirements, Purchases, Meal

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Ingredients)
admin.site.register(RecipeRequirements)
admin.site.register(Purchases)
admin.site.register(Meal)
