from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
    # one recipe can cater to many different meny items


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=200)
    ingredient_quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient_name}"


class RecipeRequirements(models.Model):
    ingredients_req = models.ForeignKey('Ingredients', on_delete=models.CASCADE)
    for_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1500, null=True)

    def __str__(self):
        return f"{self.ingredients_req}"


class Purchases(models.Model):
    item_purchased = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    quantity_purchased = models.IntegerField()

    def __str__(self):
        return f"{self.item_purchased}"


class Meal(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=10, blank = True, null = True)
    instructions = models.CharField(max_length=4000, blank = True, null = True)
    region = models.CharField(max_length=20, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

