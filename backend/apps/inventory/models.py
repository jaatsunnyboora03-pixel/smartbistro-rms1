from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=20)
    threshold = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def is_low_stock(self):
        return self.quantity <= self.threshold

class RecipeIngredient(models.Model):
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
