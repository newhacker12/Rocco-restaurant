# this is where we begin.
from django import forms
from .models import MenuItem, Ingredients, Purchases, RecipeRequirements


class AddMenuItem(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


class AddtoInventory(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'


class AddRecipeRequirements(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = '__all__'


class UpdateInventory(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'


class AddPurchase(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'

