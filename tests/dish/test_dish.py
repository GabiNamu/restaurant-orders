from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("Lasanha", 25.90)
    ingredient = Ingredient("presunto")
    dish.add_ingredient_dependency(ingredient, 15)
    dish2 = Dish("Pizza", 40.00)
    dish3 = Dish("Lasanha", 25.90)

    assert dish.__repr__() == "Dish('Lasanha', R$25.90)"

    assert dish.name == "Lasanha"
    assert dish.price == 25.90
    assert dish.recipe == {ingredient: 15}

    assert dish.__hash__() != dish2.__hash__()
    assert dish.__hash__() == dish.__hash__()

    with pytest.raises(TypeError):
        Dish("Pizza", "40.00")

    with pytest.raises(ValueError):
        Dish("Pizza", 0)

    assert dish.__eq__(dish2) is False
    assert dish.__eq__(dish3) is True

    assert dish.recipe.get(ingredient) == 15

    assert dish.get_ingredients() == {ingredient}

    assert dish.get_restrictions() == ingredient.restrictions
