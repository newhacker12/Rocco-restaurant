"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurant_app import views
from restaurant_app.views import add_recipe, add_ingredient,\
    add_recipereq, add_purchase, update_inventory, view_menu, view_inventory, \
    view_purchase, view_profitrev, view_repository, view_recipereq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/list', view_menu, name='menulist'),
    path('inventory/list', view_inventory, name='inventorylist'),
    path('purchase/list', view_purchase, name='purchaselist'),
    path('profitrev/list', view_profitrev, name='profitrevlist'),
    path('ingredients/delete', views.DeleteIngredientView.as_view(),
         name='deleteingredient'), # need to edit
    path('menu/create', add_recipe, name='menucreate'),
    path('inventory/create', add_ingredient, name='inventorycreate'),
    path('recipereq/create', add_recipereq, name='recipereqcreate'),
    path('inventory/update', update_inventory, name='inventoryupdate'),
    path('purchase/add', add_purchase, name='purchasecreate'),
    path('repository/view', view_repository, name='viewrep'),
    path('recipereq/view', view_recipereq, name='viewrecipereq'),

]
