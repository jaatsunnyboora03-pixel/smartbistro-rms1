import pytest
from apps.inventory.models import Ingredient

@pytest.mark.django_db
def test_low_stock_flag():
    ingredient = Ingredient(name='Beef patty', quantity=3, unit='units', threshold=10)
    assert ingredient.is_low_stock is True

@pytest.mark.django_db
def test_sufficient_stock_flag():
    ingredient = Ingredient(name='Burger bun', quantity=50, unit='units', threshold=10)
    assert ingredient.is_low_stock is False

@pytest.mark.django_db
def test_inventory_deduction_on_order():
    ingredient = Ingredient.objects.create(name='Beef patty', quantity=10, unit='units', threshold=3)
    ingredient.quantity -= 1
    ingredient.save()
    ingredient.refresh_from_db()
    assert ingredient.quantity == 9
