from django.shortcuts import redirect, render
from .models import MenuItem, Ingredients, RecipeRequirements, Purchases, Meal
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import AddMenuItem, AddtoInventory, AddRecipeRequirements, \
    UpdateInventory, AddPurchase
import requests

# DISPLAY VIEWS


def view_menu(request):
    return render(request, "restaurant_app/menu.html", {
        "menu": MenuItem.objects.all(),
        "menu_count": MenuItem.objects.count(),
        "recipe": RecipeRequirements.objects.all()

    }) # there need to be some variables created here which you can then use in
# your html file
#


def view_recipereq(request):
    return render(request, "restaurant_app/view_recipereq.html", {


    })


def view_inventory(request):
    return render(request, "restaurant_app/ingredients.html", {
        "ingredients": Ingredients.objects.all()

    })

def view_purchase(request):
    pass

def view_profitrev(request):
    pass

def meal_detail(request, id):
    pass




def add_recipe(request):
    if request.method == "POST":
        form = AddMenuItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/menu/list")
    else:
        form = AddMenuItem()
    # so the request.POST is used when creating a new object
    return render(request, "restaurant_app/add_recipe.html", {"form": form})


def add_ingredient(request):
    if request.method == "POST":
        form = AddtoInventory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/inventory/create")
    else:
        form = AddtoInventory()
    return render(request, "restaurant_app/add_ingredients.html", {"form": form})


def add_recipereq(request):
    if request.method == "POST":
        form = AddRecipeRequirements(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/recipereq/create")
    else:
        form = AddRecipeRequirements()
    return render(request, "restaurant_app/add_recipereq.html", {"form": form})


def update_inventory(request):
    if request.method == "POST":
        form = UpdateInventory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/inventory/update")
    else:
        form = UpdateInventory()
    return render(request, "restaurant_app/update_inventory.html", {"form": form})


def add_purchase(request):
    if request.method == "POST":
        form = UpdateInventory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/purchase/add")
    else:
        form = AddPurchase()
    return render(request, "restaurant_app/add_purchase.html", {"form": form})


def view_repository(request):
    all_meals = {}
    if 'name' in request.GET: # request.GET is the data in the form
        name = request.GET['name']
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=%s' % \
              name
        response = requests.get(url)
        data = response.json()
        meals = data['meals']  # this is the entire json dictionary
        # here, you got access to the json dictionary

        for elem in meals:
            meal_data = Meal(
                name=elem['strMeal'],
                category=elem['strCategory'],
                instructions=elem['strInstructions'],
                region=elem['strArea'],
                slug=elem['idMeal'],
                image_url=elem['strMealThumb']
            )
            meal_data.save()
        # here, you looped through the json dictionary to create a Model
        # instance from the API data
            all_meals = Meal.objects.all().order_by('-id')
            # all_meals refers to a dictionary of all the mealsearch objects
            # you pass this into render so that you can access attributes of
            # meals in your template
    return render(request, "restaurant_app/extra_recipes.html", {"all_meals": all_meals})



# think about the redirects. Should we redirect all pages to menu/list? nah right

# now we need to deal with the views for just viewing the page and displaying model data









class MenuItemView(ListView):
    model = MenuItem
    template_name = "restaurant_app/menu.html"
    # you want to view the menu as a table


class InventoryView(ListView):
    model = Ingredients
    template_name = "restaurant_app/ingredients.html"
    # this is a view of the Inventory of ingredients


class PurchaseView(ListView):
    model = Purchases
    template_name = "restaurant_app/purchases.html"


class ProfitRevView(ListView):
    model = Purchases
    template_name = "restaurant_app/profit_revenue.html"


class DeleteIngredientView(DeleteView):
    model = Ingredients
    template_name = "restaurant_app/delete_ingredient.html"


# VIEWS FOR FORMS








