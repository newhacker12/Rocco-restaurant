# Generated by Django 4.0.6 on 2022-07-29 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=200)),
                ('ingredient_quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('for_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.menuitem')),
                ('ingredients_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('quantity_purchased', models.IntegerField()),
                ('item_purchased', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.menuitem')),
            ],
        ),
    ]
